# -*- coding: utf-8 -*-
# from odoo import http


# class AcademyCenter(http.Controller):
#     @http.route('/academy_center/academy_center/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy_center/academy_center/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_center.listing', {
#             'root': '/academy_center/academy_center',
#             'objects': http.request.env['academy_center.academy_center'].search([]),
#         })

#     @http.route('/academy_center/academy_center/objects/<model("academy_center.academy_center"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_center.object', {
#             'object': obj
#         })
