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

