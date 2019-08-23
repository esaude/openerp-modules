# -*- coding: utf-8 -*-
{
    'name':'POC Fields Modifier',
    'version':'1.0',
    'category' : 'base',
    'summary': 'POC Fields Modifier' ,
    'description' : """This module help to hide unnecessary fields and menus from the view.""",
    'author':'Satvix Informatics',
    'website':'https://www.satvix.com/',
    'depends':['sale','bahmni_sale_discount','bahmni_atom_feed','hr','account','mail','account_voucher','bahmni_print_bill'],
    'data': [
        'sale_view.xml',
    ],
    'js': [],
    'qweb': ['static/src/xml/*.xml'],
    'css':[],
    'demo': [],
    'images':[],
    'test': [],
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
