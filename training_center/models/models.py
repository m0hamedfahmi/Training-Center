# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Students(models.Model):
    _name = 'student.student'
    _rec_name = 'name'
    _description = 'Students Model'

    name = fields.Char(string="Student Name", required=True, )
    birth_date = fields.Date(string="Birth Date", required=True, default=fields.Date.context_today)

