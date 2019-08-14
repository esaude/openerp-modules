# -*- coding: utf-8 -*-
{
    'name':'OpenERP-Bahmni Connector',
    'version':'1.0',
    'sequence': 14,
    'category' : 'base',
    'summary': 'OpenERP-Bahmni Connector' ,
    'description' : """
      This module help to traversed data from OpenERP to Bahmni. When you convert the Quotation to Sales Order, it will send dispensed,firstArvdispensed,arvdispensed and dispenseddate to bahmni drug order using the bahmni host,database and user configuration.
    """,
    'author':'Satvix Informatics',
    'website':'https://www.satvix.com/',
    'depends':['base','product','bahmni_sale_discount'],
    'data': [
        "config_data.xml",
        "oe_bahmni_config_view.xml",
        "sale_view.xml",
    ],
    'js': [],
    'qweb': [],
    'css':[],
    'demo': [],
    'images':[],
    'test': [],
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
