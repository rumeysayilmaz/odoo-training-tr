from odoo import models, fields, api
from odoo import tools
from odoo.modules.module import get_module_resource

class Device(models.Model):
    _name = 'tracking.device'
    _description = 'Tracking iot Devices'
    _rec_name = 'device_type'

    device_type = fields.Char(string="Device Type")
    ip_address = fields.Char(string="Ip Address")
    fixed_asset_no = fields.Char(string="Fixed Asset Number")

    #movement_ids = fields.One2many('tracking.movement', 'device_id', string="Movement")
    location_id = fields.Many2one('tracking.location', string="Location")

    # the following code concatenates many2one fields on a single record
    # @api.multi
    # def name_get(self):
    #     result = []
    #
    #     for record in self:
    #         name = str(record.ip_address) + ', ' + record.fixed_asset_no
    #         result.append((record.id, name))
    #     return result
