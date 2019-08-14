# -*- coding: utf-8 -*-

{
    'name': 'Register Medication Dispensed',
    'version': '1.0',
    'summary': 'Register Medication Dispensed',
    'description': """
        As a user, I want to record the following on OpenERP when a patient is prescribed with some medicines
        This has to be done on the Sales Quotation Template:
        
        * Category (to be included once the MPOC - 316 is implemented)
        * Name of the Medication [Rename Product to Name of Medication]
        * Quantity Total
        * Quantity Dispensed
        * Date of Lifting [Rename Date and Time to Date and Time of Lifting]
		
    """,
    'author': 'Satvix Informatics',
    'website': 'http://www.satvix.com',
    'depends': ['sale','sale_stock','bahmni_stock_batch_sale_price','bahmni_sale_discount','poc_fields_modifier'],
    'category': 'Sale',
    'data': [
        'sale_order_view.xml'
    ],
    'installable': True,
    'auto_install': True,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
