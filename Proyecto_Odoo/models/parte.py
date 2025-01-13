from odoo import models, fields

class Parte(models.Model):
    _name = 'proyecto_odoo.parte'
    _description = 'Modelo de Parte'

    name = fields.Char(string='Nombre Parte', required=True)
    tipo = fields.Selection([
        ('tipo1', 'Tipo 1'),
        ('tipo2', 'Tipo 2'),
        ('tipo3', 'Tipo 3'),
    ], string='Tipo de Parte', required=True)
    peso = fields.Float(string='Peso de Parte', required=True)