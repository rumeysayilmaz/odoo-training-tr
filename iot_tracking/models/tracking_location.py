from odoo import models, fields, api
from odoo import tools
from odoo.modules.module import get_module_resource

class Location(models.Model):
    _name = 'tracking.location'
    _description = 'Locations'

    name = fields.Char(string="Location Name")

    #device_ids = fields.One2many('tracking.device', 'location_id', string="Device")
    #authorization_ids = fields.One2many('tracking.authorization', 'location_id', string="Authorization")