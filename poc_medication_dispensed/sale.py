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


class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'
    
    _columns = {
	'quantity_total': fields.float('Quantity Total', digits_compute= dp.get_precision('Product UoS')),
        'category_id': fields.related('product_id','categ_id',type='many2one',relation='product.category',string='Category', store=True, readonly=True),
    }

        
sale_order_line()
