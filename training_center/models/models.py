# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class Students(models.Model):
    _name = 'student.student'
    _rec_name = 'name'
    _inherit = ['image.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Students Model'

    name = fields.Char(string="Student Name", required=True, )
    birth_date = fields.Date(string="Birth Date", required=True, default=fields.Date.context_today)
    email = fields.Char(string="Email", required=True, )
    national_id = fields.Char(string="National ID", required=True, ) #TODO: Add constarints to check if it is 14 digits
    school_id = fields.Many2one(comodel_name="res.partner", string="School", required=False, )
    image_1920 = fields.Image(string="Image", )
    description = fields.Html(string="Description", )

    _sql_constraints = [
        ('check_length_national_id', 'check(char_length(national_id)=14)', 'Check The national ID it seems to be incorrect!'),
    ]

    @api.constrains('email')
    def email_validation(self):
        """
        A validator to check if the email is Gmail, Yahoo or Hotmail only
        """
        if '@' in self.email:
            email = self.email.split('@')[1]
        else:
            raise UserError('Invalid Email!')

        if email not in ['gmail.com', 'yahoo.com', 'hotmail.com']:
            raise ValidationError(_("Wrong Email"))

    @api.model
    def create(self, values):
        print("Create")
        print(values)
        print("============================================")
        return super(Students, self).create(values)

    def write(self, values):
        print("Write")
        print(values)
        print("============================================")
        return super(Students, self).write(values)


class Partners(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_school = fields.Boolean(string="Is School", )

