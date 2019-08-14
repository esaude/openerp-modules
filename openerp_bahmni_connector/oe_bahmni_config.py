# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class oe_bahmni_config(osv.osv_memory):
    _name = 'oe.bahmni.config'
    _inherit = 'res.config.settings'
    _columns = {
        'host': fields.char('Host', help="Bahmni Host Name(Host IP)"),
        'database': fields.char('Database', help="Database name of Bahmni"),
        'username': fields.char('Username', help="Username name of Database"),
        'password': fields.char('Password', help="Password of the above filled User"),
        'port': fields.char('Port', help="Port of the hosted ip"),
    }
    
    def get_default_host(self, cr, uid, fields, context=None):
        host = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_host').value
        return {'host': host}

    def set_default_host(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context)
        record = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_host')
        record.write({'value': config.host})
        
    def get_default_database(self, cr, uid, fields, context=None):
        database = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_database').value
        return {'database': database}

    def set_default_database(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context)
        record = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_database')
        record.write({'value': config.database})
        
    def get_default_username(self, cr, uid, fields, context=None):
        username = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_username').value
        return {'username': username}

    def set_default_username(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context)
        record = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_username')
        record.write({'value': config.username})
        
    def get_default_password(self, cr, uid, fields, context=None):
        password = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_password').value
        return {'password': password}

    def set_default_password(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context)
        record = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_password')
        record.write({'value': config.password})
        
    def get_default_port(self, cr, uid, fields, context=None):
        port = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_port').value
        return {'port': port}

    def set_default_port(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context)
        record = self.pool.get('ir.model.data').get_object(cr, uid, 'openerp_bahmni_connector', 'bahmni_port')
        record.write({'value': config.port})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
