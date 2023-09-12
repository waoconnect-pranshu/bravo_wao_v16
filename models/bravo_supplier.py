from odoo import api, fields, models, tools

class ResPartner(models.Model):
    _inherit = 'res.partner'

#   is_supplier = fields.Boolean(string='Is Supplier')
    brand = fields.Char(string='Brand Name*')