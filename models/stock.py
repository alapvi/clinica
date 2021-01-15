# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stock(models.Model):
    _name = 'clinica.stock'
    _description = 'clinica.stock'

    name = fields.Char(string="Producto",index=True,required=True)
    cantidad = fields.Integer(size=4)



