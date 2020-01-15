# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class VitPortocv(http.Controller):

	# Public
	@http.route("/index/<int:employee_id>", auth='public')
	def index(self, employee_id, **kw): # hasil parsing di masukan ke fungsi
		employee_id = request.env['hr.employee'].sudo().search([('id', '=', employee_id) ]) # employee_id dari parameter
		
		if employee_id:
			return request.render("vit_portocv.index", {
				'employee_id'	: employee_id,
			})
		else:
			return request.render("vit_portocv.not_found", {
			})

# class VitPortocv(http.Controller):

    # @http.route('/index/', auth='public')
    # def list(self, **kw):
        # return http.request.render('vit_portocv.index', {
        # })

#     @http.route('/vit_portocv/vit_portocv/objects/<model("vit_portocv.vit_portocv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_portocv.object', {
#             'object': obj
#         })