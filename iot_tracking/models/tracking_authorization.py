from odoo import models, fields, api
from odoo import tools
from odoo.modules.module import get_module_resource

class Authorization(models.Model):
    _name = 'tracking.authorization'

    expire_date = fields.Datetime(string='Expiry Date')

    partner_id = fields.Many2one('res.partner')
    object_id = fields.Many2one('tracking.deviceobject', domain="[('partner_id', '=', partner_id)]", required=True, string="IOT Code")
    location_id = fields.Many2one('tracking.location', required=True, string="Location")