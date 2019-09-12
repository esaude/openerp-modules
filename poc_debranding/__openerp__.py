# -*- coding: utf-8 -*-
{
    'name':'POC Debranding',
    'version':'1.0',
    'category' : 'web',
    'summary': 'POC Debranding' ,
    'description' : """This module help to change the login page view.""",
    'author':'Satvix Informatics',
    'website':'https://www.satvix.com/',
    'depends':[
        'web',
        'auth_signup',     
    ],
    'data': [
    ],
    'js': [],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'css':[
        "static/src/css/*.css",
    ],
    'demo': [],
    'images':[
        'static/src/img/*.png'
    ],
    'test': [],
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
