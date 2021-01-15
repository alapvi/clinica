# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historial(models.Model):
    _name = 'clinica.historial'

    fecha = fields.Datetime(string="fecha",default=fields.Datetime.now)
    detalle = fields.Html(string="detalle")
    paciente_id = fields.Many2one("clinica.paciente")
    
    
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100