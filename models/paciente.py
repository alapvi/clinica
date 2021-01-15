# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class Paciente(models.Model):
    _name = 'clinica.paciente'
    _description = 'clinica.paciente'
    _order = 'apellidos'

    dni = fields.Char('DNI',index=True,required=True, translate=False, size=9)
    foto = fields.Binary(string="Foto")
    name = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",index=True)
    telf = fields.Char(string="Teléfono", size=9)
    fechaNac = fields.Date(string="FechaNac")
    email = fields.Char(string="Email")
    historial_ids = fields.One2many("clinica.historial","paciente_id")
    visitas = fields.Integer(compute='num_visitas', store=True)
    #numVisitas = fields.Integer(string="Visitas",readonly=True)

    @api.one    
    def eliminaHistorial(self):
        _logger.info("Eliminando Historial: "+str(self.historial_ids))
        for rec in self.historial_ids:
            _logger.info("Eliminando: " + str(rec))
            rec.unlink()
        return True
    
    
    @api.one
    @api.depends('historial_ids')
    def num_visitas(self):
        _logger.info("Historial: "+str(len(self.historial_ids)))
        self.visitas = len(self.historial_ids)
        return len(self.historial_ids)

    @api.constrains('dni')
    def validate_dni(self):
        if not self.check_DNI(self.dni):
            raise ValidationError("Error en DNI!!!!")
    
    def check_DNI(self, ndni):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = ndni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False

    