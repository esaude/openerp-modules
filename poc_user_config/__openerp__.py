# -*- coding: utf-8 -*-
{
    'name':'POC User Configuration',
    'version':'1.0',
    'category' : 'base',
    'summary': 'POC User Configuration' ,
    'description' : """
      This module cover the bewlo points.

        1. By default at the time of installation of this module, it will create a Clinical,Pharmacist and Manager SESP users and set the sudo access to all of them.
        2. Load the language by default as Portuguese.
    """,
    'author':'Satvix Informatics',
    'website':'https://www.satvix.com/',
    'depends':['base','stock','account','purchase'],
    'data': [
        'portuguese_base_data.xml',
        'user_data.xml',
    ],
    'js': [],
    'css':[],
    'demo': [],
    'images':[],
    'test': [],
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
