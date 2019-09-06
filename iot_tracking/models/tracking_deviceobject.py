from odoo import models, fields, api
from odoo import tools
from odoo.modules.module import get_module_resource

class DeviceObject(models.Model):
    _name = 'tracking.deviceobject'
    _description = 'Tracking Device Objects'
    _rec_name = 'iot_code'
    name = fields.Char(string="Device Object Name")
    iot_code = fields.Char(string="IOT Code")
    _sql_constraints = [
        ('tracking_deviceobject_uq',  # Constraint unique identifier
         'UNIQUE (iot_code)',  # Constraint SQL syntax
         'IOT Code must be unique'),  # Message
    ]
    movement_ids = fields.One2many('tracking.movement', 'object_id', string="Movement")
    authorization_ids = fields.One2many('tracking.authorization', 'object_id', string="Authorization")
    partner_id = fields.Many2one('res.partner', string='Partner', store=True, readonly=False)

    # partner_id = fields.Many2one(
    #     'res.partner',
    #     delegate=True,
    #     ondelete='cascade',
    #     required=True)