# -*- coding: utf-8 -*-

import math
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp import netsvc
import datetime
    

class ir_ui_menu(osv.osv):
    _inherit = 'ir.ui.menu'

    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        menu_ids = []
        accounting_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'account', 'menu_finance')[1]
        if accounting_id:
            menu_ids.append(accounting_id)
        hr_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'hr', 'menu_hr_root')[1]
        if hr_id:
            menu_ids.append(hr_id)
        messaging_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'mail', 'mail_feeds_main')[1]
        if messaging_id:
            menu_ids.append(messaging_id)
        
        if menu_ids and len(menu_ids) > 0:
            args.append('!')
            args.append(('id', 'child_of', menu_ids))
        return super(ir_ui_menu, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)

class product_category(osv.osv):
    _inherit = "product.category"

    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name','parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            #if record['parent_id']:
            #    name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res
product_category()
