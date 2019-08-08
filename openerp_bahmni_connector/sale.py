# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp import netsvc
import logging
_logger = logging.getLogger(__name__)
import MySQLdb

class product_category(osv.osv):
    _inherit = 'product.category'
    
    _columns = {
        'is_arv': fields.boolean('ARV Category'),
    }

class sale_order(osv.osv):
    _inherit = 'sale.order'
    
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
                        cursor.execute("SELECT order_id from orders where uuid='%s'"%line.external_order_id)
                        result = cursor.fetchone()
                        if result:
                            cursor.execute("Update drug_order set dispenseddate='%s', firstArvdispensed='%s', arvdispensed='%s',dispensed='%s' where order_id=%d"%(dispenseddate,firstArvdispensed,arvdispensed,dispensed,result[0]))
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
