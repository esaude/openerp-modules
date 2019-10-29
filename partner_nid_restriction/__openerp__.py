# -*- coding: utf-8 -*-

{
    'name': 'Partner NID Restriction',
    'version': '1.0',
    'summary': 'Partner NID Restriction',
    'description': """ This module help to check the format of the NID. It should be in 18909872/09/2019/28365.
""",
    'author': 'Satvix Informatics',
    'website': 'http://www.satvix.com',
    'depends': ['sale_stock','poc_user_config'],
    'category': 'Sale',
    'data': [
        'sale_turn_around_view.xml',
        'res_partner_view.xml'
    ],
    'installable': True,
    'auto_install': True,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
