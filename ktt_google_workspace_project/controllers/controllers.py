# -*- coding: utf-8 -*-
# from odoo import http


# class KttGoogleWorkspace(http.Controller):
#     @http.route('/ktt_google_workspace/ktt_google_workspace', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ktt_google_workspace/ktt_google_workspace/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ktt_google_workspace.listing', {
#             'root': '/ktt_google_workspace/ktt_google_workspace',
#             'objects': http.request.env['ktt_google_workspace.ktt_google_workspace'].search([]),
#         })

#     @http.route('/ktt_google_workspace/ktt_google_workspace/objects/<model("ktt_google_workspace.ktt_google_workspace"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ktt_google_workspace.object', {
#             'object': obj
#         })

