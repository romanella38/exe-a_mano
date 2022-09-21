# -*- coding: utf-8 -*-
# from odoo import http


# class AMano(http.Controller):
#     @http.route('/a_mano/a_mano/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/a_mano/a_mano/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('a_mano.listing', {
#             'root': '/a_mano/a_mano',
#             'objects': http.request.env['a_mano.a_mano'].search([]),
#         })

#     @http.route('/a_mano/a_mano/objects/<model("a_mano.a_mano"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('a_mano.object', {
#             'object': obj
#         })
