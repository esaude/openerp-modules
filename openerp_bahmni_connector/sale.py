# -*- coding: utf-8 -*-

from datetime import date,datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp import tools
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp import netsvc
import logging
_logger = logging.getLogger(__name__)
import MySQLdb
from itertools import groupby
from psycopg2._psycopg import DATETIME
from openerp import netsvc
from openerp.tools import pickle
from openerp.tools.misc import ustr
import uuid
import psycopg2
import psycopg2.extras

class product_category(osv.osv):
    _inherit = 'product.category'
    
    _columns = {
        'is_arv': fields.boolean('ARV Category'),
    }

class order_save_service(osv.osv):
    _inherit = 'order.save.service'
    
    def _create_sale_order(self, cr, uid, cus_id, name, shop_id, orders, care_setting, provider_name,location_name, context=None):
        sale_order = {
            'partner_id': cus_id,
            'name': name,
            'origin': 'ATOMFEED SYNC',
            'date_order': date.today(),
            'shop_id': shop_id,
            'partner_invoice_id': cus_id,
            'partner_shipping_id': cus_id,
            'order_policy': 'manual',
            'pricelist_id': 1,
            'care_setting' : care_setting,
            'provider_name' : provider_name,
            'location_name': location_name
        }
        if(orders):
            sale_order_id = self.pool.get('sale.order').create(cr, uid, sale_order, context=context)
            sale_order = self.pool.get('sale.order').browse(cr, uid, sale_order_id, context=context)
            for order in orders:
                self._process_orders(cr, uid, name, sale_order, orders, order, context=context)
    
    def create_orders(self, cr,uid,vals,context):
        customer_id = vals.get("customer_id")
        location_name = vals.get("locationName")
        all_orders = self._get_openerp_orders(vals)

        if(not all_orders):
            return ""

        customer_ids = self.pool.get('res.partner').search(cr, uid, [('ref', '=', customer_id)], context=context)
        if(customer_ids):
            cus_id = customer_ids[0]

            for orderType, ordersGroup in groupby(all_orders, lambda order: order.get('type')):

                orders = list(ordersGroup)
                care_setting = orders[0].get('visitType').lower()
                provider_name = orders[0].get('providerName')
                unprocessed_orders = self._filter_processed_orders(context, cr, orders, uid)

                tup = self._get_shop_and_local_shop_id(cr, uid, orderType, location_name, context)
                shop_id = tup[0]
                local_shop_id = tup[1]

                if(not shop_id):
                    continue

                name = self.pool.get('ir.sequence').get(cr, uid, 'sale.order')
                #Adding both the ids to the unprocessed array of orders, Separating to dispensed and non-dispensed orders
                unprocessed_dispensed_order = []
                unprocessed_non_dispensed_order = []
                for unprocessed_order in unprocessed_orders :
                    unprocessed_order['custom_shop_id'] = shop_id
                    unprocessed_order['custom_local_shop_id'] = local_shop_id
                    if(unprocessed_order.get('dispensed', 'false') == 'true') :
                        unprocessed_dispensed_order.append(unprocessed_order)
                    else :
                        unprocessed_non_dispensed_order.append(unprocessed_order)

                if(len(unprocessed_non_dispensed_order) > 0 ) :
                    sale_order_ids = self.pool.get('sale.order').search(cr, uid, [('partner_id', '=', cus_id), ('shop_id', '=', unprocessed_non_dispensed_order[0]['custom_shop_id']), ('state', '=', 'draft'), ('origin', '=', 'ATOMFEED SYNC')], context=context)

                    if(not sale_order_ids):
                        #Non Dispensed New
                        self._create_sale_order(cr, uid, cus_id, name, unprocessed_non_dispensed_order[0]['custom_shop_id'], unprocessed_non_dispensed_order, care_setting, provider_name,location_name,context)
                    else:
                        #Non Dispensed Update
                        self._update_sale_order(cr, uid, cus_id, name, unprocessed_non_dispensed_order[0]['custom_shop_id'], care_setting, sale_order_ids[0], unprocessed_non_dispensed_order, provider_name, context)

                    sale_order_ids_for_dispensed = self.pool.get('sale.order').search(cr, uid, [('partner_id', '=', cus_id), ('shop_id', '=', unprocessed_non_dispensed_order[0]['custom_local_shop_id']), ('state', '=', 'draft'), ('origin', '=', 'ATOMFEED SYNC')], context=context)

                    if(len(sale_order_ids_for_dispensed) > 0):
                        if(sale_order_ids_for_dispensed[0]) :
                            sale_order_line_ids_for_dispensed = self.pool.get('sale.order.line').search(cr, uid, [('order_id', '=', sale_order_ids_for_dispensed[0])], context=context)
                            if(len(sale_order_line_ids_for_dispensed) == 0):
                                self.pool.get('sale.order').unlink(cr, uid, sale_order_ids_for_dispensed, context=context)


                if(len(unprocessed_dispensed_order) > 0 and local_shop_id) :
                    sale_order_ids = self.pool.get('sale.order').search(cr, uid, [('partner_id', '=', cus_id), ('shop_id', '=', unprocessed_dispensed_order[0]['custom_shop_id']), ('state', '=', 'draft'), ('origin', '=', 'ATOMFEED SYNC')], context=context)

                    sale_order_ids_for_dispensed = self.pool.get('sale.order').search(cr, uid, [('partner_id', '=', cus_id), ('shop_id', '=', unprocessed_dispensed_order[0]['custom_local_shop_id']), ('state', '=', 'draft'), ('origin', '=', 'ATOMFEED SYNC')], context=context)

                    if(not sale_order_ids_for_dispensed):
                        #Remove existing sale order line
                        self._remove_existing_sale_order_line(cr,uid,sale_order_ids[0],unprocessed_dispensed_order,context=context)

                        #Removing existing empty sale order
                        sale_order_line_ids = self.pool.get('sale.order.line').search(cr, uid, [('order_id', '=', sale_order_ids[0])], context=context)

                        if(len(sale_order_line_ids) == 0):
                            self.pool.get('sale.order').unlink(cr, uid, sale_order_ids, context=context)

                        #Dispensed New
                        self._create_sale_order(cr, uid, cus_id, name, unprocessed_dispensed_order[0]['custom_local_shop_id'], unprocessed_dispensed_order, care_setting, provider_name,location_name,context)

                        if(self._allow_automatic_convertion_to_saleorder (cr,uid)):
                            sale_order_ids_for_dispensed = self.pool.get('sale.order').search(cr, uid, [('partner_id', '=', cus_id), ('shop_id', '=', unprocessed_dispensed_order[0]['custom_local_shop_id']), ('state', '=', 'draft'), ('origin', '=', 'ATOMFEED SYNC')], context=context)
                            self.pool.get('sale.order').action_button_confirm(cr, uid, sale_order_ids_for_dispensed, context)

                    else:
                        #Remove existing sale order line
                        self._remove_existing_sale_order_line(cr,uid,sale_order_ids[0],unprocessed_dispensed_order,context=context)

                        #Removing existing empty sale order
                        sale_order_line_ids = self.pool.get('sale.order.line').search(cr, uid, [('order_id', '=', sale_order_ids[0])], context=context)
                        if(len(sale_order_line_ids) == 0):
                            self.pool.get('sale.order').unlink(cr, uid, sale_order_ids, context=context)

                        #Dispensed Update
                        self._update_sale_order(cr, uid, cus_id, name, unprocessed_dispensed_order[0]['custom_local_shop_id'], care_setting, sale_order_ids_for_dispensed[0], unprocessed_dispensed_order, provider_name, context)
        else:
            raise osv.except_osv(('Error!'), ("Patient Id not found in openerp"))

class sale_order(osv.osv):
    _inherit = 'sale.order'
    
    _columns = {
        'location_name': fields.char('Location Name', size=64),
    }
    
    def action_button_confirm(self, cr, uid, ids, context=None):
        ir_model_data = self.pool.get('ir.model.data')
        config_parameter_pool = self.pool.get('ir.config_parameter')
        
        host_parameter_id = ir_model_data.get_object_reference(cr, uid, 'openerp_bahmni_connector', 'bahmni_host')[1]
        db_parameter_id = ir_model_data.get_object_reference(cr, uid, 'openerp_bahmni_connector', 'bahmni_database')[1]
        user_parameter_id = ir_model_data.get_object_reference(cr, uid, 'openerp_bahmni_connector', 'bahmni_username')[1]
        pwd_parameter_id = ir_model_data.get_object_reference(cr, uid, 'openerp_bahmni_connector', 'bahmni_password')[1]
        port_parameter_id = ir_model_data.get_object_reference(cr, uid, 'openerp_bahmni_connector', 'bahmni_port')[1]
        
        host = config_parameter_pool.browse(cr,uid,host_parameter_id,context=context).value
        database = config_parameter_pool.browse(cr,uid,db_parameter_id,context=context).value
        username = config_parameter_pool.browse(cr,uid,user_parameter_id,context=context).value
        password = config_parameter_pool.browse(cr,uid,pwd_parameter_id,context=context).value
        port = config_parameter_pool.browse(cr,uid,port_parameter_id,context=context).value
        
        try:
            db = MySQLdb.connect(host=host, port=int(port), user=username, passwd=password, db=database)
            cursor = db.cursor()
            
            now = datetime.now()
            dispenseddate = now.strftime("%Y-%m-%d %H:%M:%S")
            firstArvdispensed = 1
            
            
            sale_order_obj = self.browse(cr,uid,ids[0])
            pre_order_ids = self.search(cr,uid,[('partner_id', '=', sale_order_obj.partner_id.id)],context=context)
            if pre_order_ids:
                if len(pre_order_ids) > 1:
                    firstArvdispensed = 0
            
            if sale_order_obj.order_line:
                for line in sale_order_obj.order_line:
                    if line.external_order_id:
                        arvdispensed = 0
                        dispensed = 1
                        
                        if line.product_id.categ_id.is_arv:
                            arvdispensed = 1
                        # For concept ID
                        cursor.execute("select concept_id from concept_name where name='dispensed'")
                        concept_result = cursor.fetchone()
                        # For Person Attribute Type
                        cursor.execute("select person_attribute_type_id from person_attribute_type where name='PATIENT_STATUS'")
                        person_attribute_result = cursor.fetchone()
                        # For TARV Concept ID
                        cursor.execute("select concept_id from concept_name where name='TARV'")
                        tarv_concept_result = cursor.fetchone()
                        # For TPRE-ARV Concept ID
                        cursor.execute("select concept_id from concept_name where name='Pre TARV'")
                        pretarv_concept_result = cursor.fetchone()
                        
                        
                        
                        # For Orders
                        cursor.execute("SELECT patient_id,encounter_id,order_id,creator,voided from orders where uuid='%s'"%line.external_order_id)
                        order_result = cursor.fetchone()
                        
                        # For update Person Attributes
                        cursor.execute("update person_attribute set value=%d where person_id=%d and person_attribute_type_id=%d and value=%d"%(tarv_concept_result[0],order_result[0],person_attribute_result[0],pretarv_concept_result[0]))
                        
                        # For update Person UUID
                        cursor.execute("SELECT uuid from person where person_id='%d'"%order_result[0])
                        person_uuid_result = cursor.fetchone()
                        
                        location_name = ''
                        if sale_order_obj.location_name:
                            location_name = sale_order_obj.location_name
                        
                        # For Location ID
                        cursor.execute("SELECT location_id from location where name='%s'"%location_name)
                        location_name_result = cursor.fetchone()
                        
                        
                        
                        if order_result and location_name_result:
                            # Insert in OBS Table
                            cursor.execute("INSERT INTO obs(person_id,concept_id,encounter_id,order_id,obs_datetime,status,uuid,creator, date_created,voided,value_coded,location_id) values (%d,%d,%d,%d,now(),'FINAL',UUID(),%d,now(),%d,1,%d) " %(order_result[0],concept_result[0],order_result[1],order_result[2],order_result[3],order_result[4],location_name_result[0]))
                            # Insert into ERPDrug_Order
                            
                            cursor.execute("INSERT INTO erpdrug_order(order_id,patient_id,dispensed,arvdispensed,firstArvdispensed,dispenseddate,encounter_id,location_id,creator,date_created,uuid) values (%d,%d,%s,%s,%s,now(),%d,%d,%d,now(),UUID())" %(order_result[2],order_result[0],dispensed,arvdispensed,arvdispensed,order_result[1],location_name_result[0],order_result[3]))
                            db.commit()
        except MySQLdb.Error, e:
            _logger.error("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            if cursor and db:
                cursor.close()
                db.close()
        return super(sale_order, self).action_button_confirm(cr, uid, ids, context=context)

sale_order()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
