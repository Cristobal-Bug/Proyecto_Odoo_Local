from odoo import models, fields

class Producto(models.Model):
    _name = 'proyecto_odoo.producto'
    _description = 'Modelo de Producto'

    name = fields.Char(string='Nombre Producto', required=True)
    codigo = fields.Char(string='Código Producto', required=True)
    periodo_id = fields.Many2one('proyecto_odoo.periodo', string='Periodo', required=True)
    partes_ids = fields.Many2many('proyecto_odoo.parte', string='Listado de Partes')