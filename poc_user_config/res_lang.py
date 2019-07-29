# -*- coding: utf-8 -*-

import locale
from locale import localeconv
import logging
import re
import openerp
import datetime
from lxml import etree
import math
import pytz

from openerp.tools.safe_eval import safe_eval as eval
from openerp import SUPERUSER_ID
from openerp import pooler, tools
from openerp.osv import osv, fields
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    def create(self, cr, uid, vals, context=None):
        vals.update({'lang':'pt_PT'})
        modobj = self.pool.get('ir.module.module')
        mids = modobj.search(cr, uid, [('state', '=', 'installed')])
        context = {'overwrite': True}
        modobj.update_translations(cr, uid, mids, 'pt_PT', context or {})
        admin_partner_id = self.pool['ir.model.data'].get_object_reference(cr, uid, 'base', 'partner_root')[1]
        cr.execute('UPDATE res_partner SET lang=%s where id=%s', ('pt_PT',admin_partner_id,))
        admin = self.browse(cr,uid,admin_partner_id)
        print "\n\n=DONE====",admin.lang
        return super(res_partner, self).create(cr, uid, vals, context=context)
    
res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
