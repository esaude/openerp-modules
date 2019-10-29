# -*- coding: utf-8 -*-
{
    'name':'POC Translation: PORTUGUESE',
    'version':'1.0',
    'sequence': 14,
    'category' : 'base',
    'summary': 'POC Translation: PORTUGUESE' ,
    'description' : """
      This module Translate lables in PORTUGUESE language.
    """,
    'author':'Satvix Informatics',
    'website':'https://www.satvix.com/',
    'depends':[
        'base',
        'sale',
        'bahmni_sale_discount',
        'bahmni_stock_batch_sale_price',
        'sale_stock',
        'bahmni_atom_feed',
        'bahmni_print_bill',
        'bahmni_purchase_extension',
        'purchase',
        'mail',
        'stock',
        'bahmni_customer_payment',
        ],
    'data': ["add_invoice_print_button.xml"],
    'js': [],
    'qweb': ['static/src/xml/print.xml'],
    'css':[],
    'demo': [],
    'images':[],
    'test': [],
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
