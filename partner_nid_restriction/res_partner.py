# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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


class res_partner(osv.osv):
    _inherit = 'res.partner'

    def create(self, cr, uid, vals, context=None):
        result = super(res_partner, self).create(cr, uid, vals, context=context)
        print "\n\n==========result",result
        partner_obj = self.browse(cr,uid,result,context=context)
        if partner_obj.ref:
            ref_data = partner_obj.ref.split('/')
            if len(ref_data) == 4:
                if len(ref_data[0]) != 8 or len(ref_data[1]) != 2 or len(ref_data[2]) != 4 or len(ref_data[3]) != 5:
                    raise osv.except_osv(_('Error!'), _('NID format is invalid !'))
            else:
                raise osv.except_osv(_('Error!'), _('NID format is invalid !'))
        return result
        
    
    def write(self, cr, uid, ids, vals, context=None):
        if vals.has_key('ref') and vals.get('ref'):
            ref_data = vals.get('ref').split('/')
            if len(ref_data) == 4:
                if len(ref_data[0]) != 8 or len(ref_data[1]) != 2 or len(ref_data[2]) != 4 or len(ref_data[3]) != 5:
                    raise osv.except_osv(_('Error!'), _('NID format is invalid !'))
            else:
                raise osv.except_osv(_('Error!'), _('NID format is invalid !'))
        return super(res_partner, self).write(cr, uid, ids, vals, context=context)

        
res_partner()
