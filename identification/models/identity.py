from odoo import fields, models
from odoo.exceptions import Warning

class Identification(models.Model):

    _name ='identification'
    _description = 'Identification'

    employee_name = fields.Many2one("hr.employee", required=True)
    id_number = fields.Char(string='ID Number')
    identity_type = fields.Selection([('passport', 'Passport'),('id_card', 'ID_Card'),('driving license','Driving License')],string='Type',default='to_translate',help="Employee Identification Details")

    # @api.multi
    # def button_check_id_number(self):
    #     for employee_identity.id_number in self:
    #         if not employee_identity.id_number:
    #         raise Warning('Please provide an ID number for %s' % employee_identity.employee_name)
    #     return True


