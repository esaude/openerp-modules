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
 
                 #2160201 Email
                email = self.pool.get('ir.translation').search(cr, uid, [('module','=','base'),
                                                                 ('type','=','field'),
                                                                 ('name','=','res.partner,email'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Email')], context=context)
                print("\n email",email)
                if email:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (email))
                

                #Customer Payment Term
                customer_payment_term = self.pool.get('ir.translation').search(cr, uid, [('module','=','account'),
                                                                 ('type','=','field'),
                                                                 ('name','=','res.partner,property_payment_term'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Customer Payment Term')], context=context)
                print("\n Customer Payment Term",customer_payment_term)
                if customer_payment_term:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (customer_payment_term))

                #Supplier Payment Term
                supplier_payment_term = self.pool.get('ir.translation').search(cr, uid, [('module','=','account'),
                                                                 ('type','=','field'),
                                                                 ('name','=','res.partner,property_supplier_payment_term'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Supplier Payment Term')], context=context)
                print("\n supplier_payment_term",supplier_payment_term)
                if supplier_payment_term:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (supplier_payment_term))

                #Time
                time = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking,date'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Time')], context=context)
                print("\n time",time)
                if time:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (time))

                time_in = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking.in,date'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Time')], context=context)
                print("\n time_in",time_in)
                if time_in:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (time_in))

                time_out = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking.out,date'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Time')], context=context)
                print("\n time_out",time_out)
                if time_out:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (time_out))

                #Supplier Invoice Number
                supplier_invoice_number = self.pool.get('ir.translation').search(cr, uid, [('module','=','account'),
                                                                 ('type','=','field'),
                                                                 ('name','=','account.invoice,supplier_invoice_number'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Supplier Invoice Number')], context=context)
                print("\n Supplier Invoice Number",supplier_invoice_number)
                if supplier_invoice_number:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (supplier_invoice_number))

                #Payment Reference
                payment_reference = self.pool.get('ir.translation').search(cr, uid, [('module','=','account'),
                                                                 ('type','=','field'),
                                                                 ('name','=','account.invoice,reference_type'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Payment Reference')], context=context)
                print("\n Payment Reference",payment_reference)
                if payment_reference:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (payment_reference))

                #Subtotal
                subtotal = self.pool.get('ir.translation').search(cr, uid, [('module','=','account'),
                                                                 ('type','=','field'),
                                                                 ('name','=','account.invoice,amount_untaxed'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Subtotal')], context=context)
                print("\n Subtotal",subtotal)
                if subtotal:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (subtotal))


                #Auto-Picking / Picking auto
                auto_picking = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking,auto_picking'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Auto-Picking')], context=context)
                print("\n auto_picking",auto_picking)
                if auto_picking:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (auto_picking))

                #Auto-Picking / Picking auto
                auto_picking_in = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking.in,auto_picking'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Auto-Picking')], context=context)
                print("\n auto_picking_in",auto_picking_in)
                if auto_picking_in:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (auto_picking_in))

                #Auto-Picking / Picking auto
                auto_picking_out = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking.out,auto_picking'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Auto-Picking')], context=context)
                print("\n auto_picking_out",auto_picking_out)
                if auto_picking_out:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (auto_picking_out))
                    
                #Destination Warehouse in On incoming shipment
                d_w = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','field'),
                                                                 ('name','=','stock.picking.in,warehouse_id'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Destination Warehouse')], context=context)
                print("\n Destination Warehouse in On incoming shipment",d_w)
                if d_w:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (d_w))

                #Date of Reception
                date_of_reception = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','view'),
                                                                 ('name','=','stock.picking.in'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Date of Reception')], context=context)
                print("\n Date of Reception ",date_of_reception)
                if date_of_reception:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (date_of_reception))
                   

                #Request Procurement
                request_procurement = self.pool.get('ir.translation').search(cr, uid, [('module','=','procurement'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Request Procurement')], context=context)
                print("\n Request Procurement ",request_procurement)
                if request_procurement:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (request_procurement))

                #Orderpoints
                orderpoints = self.pool.get('ir.translation').search(cr, uid, [('module','=','procurement'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Orderpoints')], context=context)
                print("\n Orderpoints ",orderpoints)
                if orderpoints:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (orderpoints))

                #Inventory
                inventory = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Inventory')], context=context)
                print("\n Inventory : ",inventory)
                if inventory:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (inventory))

                #Sales
                sales = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Sales')], context=context)
                print("\n Sales : ",sales)
                if sales:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (sales))

                #Supply Method
                supply_method = self.pool.get('ir.translation').search(cr, uid, [('module','=','procurement'),
                                                                 ('type','=','field'),
                                                                 ('name','=','product.template,supply_method'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Supply Method')], context=context)
                print("\n Supply Method : ",supply_method)
                if supply_method:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (supply_method))

                #Purchase
                purchase_group_str = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Purchase')], context=context)
                print("\n Purchase : ",purchase_group_str)
                if purchase_group_str:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (purchase_group_str))

                #Suppliers
                suppliers_group_str = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Suppliers')], context=context)
                print"\n Suppliers : ",suppliers_group_str
                if suppliers_group_str:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (suppliers_group_str))

                '''#Unit Price
                unit_price = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','field'),
                                                                 ('name','=','pricelist.partnerinfo,price'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Unit Price')], context=context)
                print"\n Unit Price : ",unit_price
                if unit_price:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (unit_price))'''

                #Description for Suppliers
                description_for_suppliers = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Description for Suppliers')], context=context)
                print"\n Description for Suppliers : ",description_for_suppliers
                if description_for_suppliers:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (description_for_suppliers))

                #Can be Purchased
                can_be_purchased = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','field'),
                                                                 ('name','=','product.template,purchase_ok'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Can be Purchased')], context=context)
                print"\n Can be Purchased : ",can_be_purchased
                if can_be_purchased:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (can_be_purchased))

                #Can be Purchased 
                can_be_purchased_view = self.pool.get('ir.translation').search(cr, uid, [('module','=','purchase'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Can be Purchased')], context=context)
                print"\n Can be Purchased View: ",can_be_purchased_view
                if can_be_purchased_view:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (can_be_purchased_view))

                #Outgoing
                outgoing = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','field'),
                                                                 ('name','=','product.product,outgoing_qty'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Outgoing')], context=context)
                print"\n Outgoing: ",outgoing
                if outgoing:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (outgoing))

                #Forecasted Quantity
                forecasted_quantity = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','field'),
                                                                 ('name','=','product.product,virtual_available'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Forecasted Quantity')], context=context)
                print"Forecasted Quantity: ",forecasted_quantity
                if forecasted_quantity:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (forecasted_quantity))

                #Case
                Case = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','product.template,loc_case'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Case')], context=context)
                print"Case: ",Case
                if Case:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (Case))

                #Sale Conditions
                Sale_Conditions = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Sale Conditions')], context=context)
                print"Sale Conditions: ",Sale_Conditions
                if Sale_Conditions:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (Sale_Conditions))

                #Customer Lead Time
                Customer_Lead_Time = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','field'),
                                                                 ('name','=','product.template,sale_delay'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Customer Lead Time')], context=context)
                print"Customer Lead Time: ",Customer_Lead_Time
                if Customer_Lead_Time:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (Customer_Lead_Time))

                #Description for Quotations
                Description_for_Quotations = self.pool.get('ir.translation').search(cr, uid, [('module','=','product'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.product'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Description for Quotations')], context=context)
                print"Description for Quotations : ",Description_for_Quotations
                if Description_for_Quotations:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (Description_for_Quotations))

                #Account Stock Properties
                Account_Stock_Properties = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','view'),
                                                                 ('name','=','product.category'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Account Stock Properties')], context=context)
                print"Account Stock Properties: ",Account_Stock_Properties
                if Account_Stock_Properties:
                    cr.execute('DELETE FROM ir_translation WHERE id = %s', (Account_Stock_Properties))

                    
                #Incoming  Products menu from the Purchase Order
                incoming_product_menus = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.ui.menu,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Incoming  Products')], context=context)
                if incoming_product_menus:
                    cr.execute('UPDATE ir_translation set value=%s WHERE id=%s', ('Produtos recebidos',tuple(incoming_product_menus)))
                    
                #Incoming  Products action from the Purchase Order
                incoming_product_action = self.pool.get('ir.translation').search(cr, uid, [('module','=','stock'),
                                                                 ('type','=','model'),
                                                                 ('name','=','ir.actions.act_window,name'),
                                                                 ('lang','=','pt_PT'),
                                                                 ('src','=','Incoming  Products')], context=context)
                if incoming_product_action:
                    cr.execute('UPDATE ir_translation set value=%s WHERE id=%s', ('Produtos recebidos',tuple(incoming_product_action)))


        return super(module, self).write(cr, uid, ids, vals, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
