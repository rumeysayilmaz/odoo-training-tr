from odoo import models, fields, api
from odoo import tools
from odoo.modules.module import get_module_resource

class Movement(models.Model):
    _name = 'tracking.movement'

    trackDateTime = fields.Datetime(string="Track Date Time", default=fields.Datetime.now())
    direction_type = fields.Char(string="Device Direction")
    partner_name = fields.Char(related='object_id.partner_id.name')

    device_id = fields.Many2one('tracking.device', string="Device")
    object_id = fields.Many2one('tracking.deviceobject', string="Device Object")

    @api.model
    def register_attendance(self, card_code, device_code):

        res = {
            'rfid_card_code': card_code,
            'employee_name': '',
            'employee_id': False,
            'error_message': '',
            'logged': False,
            'action': 'FALSE',
        }

        card = self.env["tracking.deviceobject"].search([('iot_code', '=', card_code)], limit=1)
        device = self.env["tracking.device"].search([('ip_address', '=', device_code)], limit=1)
        if card and device:
            self.env["tracking.movement"].create({
                "device_id": device.id,
                "object_id": card.id,
                "direction": "",
                "trackDateTime": fields.Datetime.now()
            })
        res["action"] = "check_in"
        return res


