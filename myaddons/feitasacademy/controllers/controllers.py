# -*- coding: utf-8 -*-
from odoo import http

# class Feitasacademy(http.Controller):
#     @http.route('/feitasacademy/feitasacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feitasacademy/feitasacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feitasacademy.listing', {
#             'root': '/feitasacademy/feitasacademy',
#             'objects': http.request.env['feitasacademy.feitasacademy'].search([]),
#         })

#     @http.route('/feitasacademy/feitasacademy/objects/<model("feitasacademy.feitasacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feitasacademy.object', {
#             'object': obj
#         })