# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp import pooler

class module(osv.osv):
    _inherit = 'ir.module.module'

    def write(self, cr, uid, ids, vals, context=None):
        if vals.has_key('state') and vals.get('state'):
            if vals.get('state') == 'installed':
                #print("vals.get('state')",vals.get('state'))
                #Messaging
                messaging_ids = self.pool.get('ir.translation').search(cr, uid, [('module','=','mail'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.ui.menu,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Messaging')], context=context)
                #print"Messaging : ",messaging_ids
                if messaging_ids:
                    cr.execute('DELETE FROM ir_translation WHERE id in %s', (tuple(messaging_ids),))

                #Send by EMail
                translation_id = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','purchase.order'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Send by EMail')], context=context)
                #print("translation_id for Send by EMail Button",translation_id)
                if translation_id:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (translation_id))

                #Confirm Order
                confirm_btn_id = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','purchase.order'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Confirm Order')], context=context)
                #print("confirm_btn_id for Confirm Order Button",confirm_btn_id)
                if confirm_btn_id:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (confirm_btn_id)) 

                #Destination Warehouse
                destination_warehouse_id = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','field'),
                                                                 ('name','=','purchase.order,warehouse_id'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Destination Warehouse')], context=context)
                #print("destination_warehouse_id for Destination Warehouse ",destination_warehouse_id)
                if destination_warehouse_id:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (destination_warehouse_id))


                #On Draft Invoices
                on_draft_invoices_id = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.ui.menu,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','On Draft Invoices')], context=context)
                #print("on_draft_invoices_id On Draft Invoicesfor",on_draft_invoices_id)
                if on_draft_invoices_id:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (on_draft_invoices_id))

                #On Purchase Order Lines
                on_purchase_order_lines = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.ui.menu,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','On Purchase Order Lines')], context=context)
                #print("on_purchase_order_lines for On Purchase Order Lines ",on_purchase_order_lines)
                if on_purchase_order_lines:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (on_purchase_order_lines))

                #On Incoming Shipments
                on_incoming_shipments = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.ui.menu,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','On Incoming Shipments')], context=context)
                #print("on_incoming_shipments for On Incoming Shipments : ",on_incoming_shipments)
                if on_incoming_shipments:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (on_incoming_shipments))

                #Customer Address
                customer_address = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','purchase.order'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Customer Address')], context=context)
                #print("Customer Address : ",customer_address)
                if customer_address:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (customer_address))

                #Invoice Received
                invoice_received = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','field'),
                                                                 ('name','=','purchase.order,invoiced'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Invoice Received')], context=context)
                #print("Invoice Received : ",invoice_received)
                if invoice_received:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (invoice_received))

                #Payment Term
                payment_term = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','field'),
                                                                 ('name','=','purchase.order,payment_term_id'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Payment Term')], context=context)
                #print("Payment Term : ",payment_term)
                if payment_term:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (payment_term))


                #Receive Invoice
                receive_invoice = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','purchase.order'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Receive Invoice')], context=context)
                #print("Receive Invoice : ",receive_invoice)
                if receive_invoice:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (receive_invoice))

                #Purchase Order 
                purchase_order = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','purchase.order'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Purchase Order ')], context=context)
                #print("Purchase Order  : ",purchase_order)
                if purchase_order:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (purchase_order))

                
                #Request for Quotation 
                rfq = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','purchase.order'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Request for Quotation ')], context=context)
                #print("Request for Quotation : ",rfq)
                if rfq:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (rfq))
                
                #Unit of Measure Categories 
                unit_of_measure_categories = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.actions.act_window,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Unit of Measure Categories')], context=context)
                #print("Unit of Measure Categories : ",unit_of_measure_categories)
                if unit_of_measure_categories:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (unit_of_measure_categories))

                #Unit of Measure Categories Second
                unit_of_measure_categories_2 = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.ui.menu,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Unit of Measure Categories')], context=context)
                #print("Unit of Measure Categories 2: ",unit_of_measure_categories_2)
                if unit_of_measure_categories_2:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (unit_of_measure_categories_2))
                    
                    
                #_Receive button from the Receive product wizard of Incoming Shipment of Purchase Order
                receive_button = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','code'),
                                                                 ('name','=','addons/stock/wizard/stock_partial_picking.py'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','_Receive')], context=context)
                if receive_button:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (receive_button))
                    
                #Subtotal field from the Sale Order Line
                so_subtotal_field = self.pool.get('ir.translation').search(cr, uid, [('module','=','sale'),
                                                                 ('type','=','field'),
                                                                 ('name','=','sale.order.line,price_subtotal'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Subtotal')], context=context)
                if so_subtotal_field:
                    cr.execute('UPDATE ir_translation set value=%s WHERE id=%s', ('Sub Total',tuple(so_subtotal_field)))
                    
                #Subtotal field from the Purchase Order Line
                po_subtotal_field = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','field'),
                                                                 ('name','=','purchase.order.line,price_subtotal'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Subtotal')], context=context)
                if po_subtotal_field:
                    cr.execute('UPDATE ir_translation set value=%s WHERE id=%s', ('Sub Total',tuple(po_subtotal_field)))
                    
        return super(module, self).write(cr, uid, ids, vals, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
