from odoo import models, fields, api
from odoo import tools
from odoo.modules.module import get_module_resource

class Movement(models.Model):
    _name = 'tracking.movement'

    trackDateTime = fields.Datetime(string="Track Date Time", default=fields.Datetime.now)
    partner_id = fields.Char(related='object_id.partner_id.name')

    device_id = fields.Many2one('tracking.device', string="Device")
    object_id = fields.Many2one('tracking.deviceobject', string="Device Object")
