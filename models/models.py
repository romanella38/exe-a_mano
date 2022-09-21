# -*- coding: utf-8 -*-

from odoo import models, fields, api


class a_mano(models.Model):
    _inherit = 'stock.quant'

   
    precio_id = fields.Float('Precio', related='product_tmpl_id.list_price')
    costo_id = fields.Float('Costo', related='product_tmpl_id.standard_price')
    


#     _name = 'a_mano.a_mano'
#     _description = 'a_mano.a_mano'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
