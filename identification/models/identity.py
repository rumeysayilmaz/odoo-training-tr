from odoo import fields, models

class Identification(models.Model):

    _name ='identification'
    _description = 'Identification'

    employee_name = fields.Many2one("hr.employee", required=True)
    id_number = fields.Char(string='ID Number')
    identity_type = fields.Selection([('passport', 'Passport'),('id_card', 'ID_Card'),('driving license','Driving License')],string='Type',default='to_translate',help="Employee Identification Details")

