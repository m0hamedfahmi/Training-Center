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
    age = fields.Integer(string="Age", compute="_compute_age", )
    email = fields.Char(string="Email", required=True, )
    national_id = fields.Char(string="National ID", required=True, ) #TODO: Add constarints to check if it is 14 digits
    school_id = fields.Many2one(comodel_name="res.partner", string="School", required=False, )
    school_email = fields.Char(string="School Email", required=False, help="email should be gmail or ...",)
    related_school_email = fields.Char(string="School Email (Related)", related="school_id.email", required=False, help="email should be gmail or ...",)
    # related_email = fields.Char(related="school_id.email")
    image_1920 = fields.Image(string="Image", )
    description = fields.Html(string="Description", )
    priority = fields.Selection(string="Priority", selection=[('0', 'Low'), ('1', 'Medium'), ('2', 'High'),('3', 'Extra')], required=False, )
    tag_ids = fields.Many2many(comodel_name="student.tag", relation="student_student_student_tag_rel", column1="student_id", column2="tag_id", string="Tags", )

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            age = fields.Date.context_today(rec) - rec.birth_date
            rec.age = age.days / 365

    @api.onchange('school_id')
    def onchange_school_id(self):
        self.school_email = self.school_id.email
        if self.school_id.email:

            if '@' in self.school_email:
                email = self.school_email.split('@')[1]
                if email not in ['gmail.com', 'yahoo.com', 'hotmail.com']:
                    return {
                        'warning': {'title': "Warning: Wrong Email", 'message': "What is this?"},
                    }

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

