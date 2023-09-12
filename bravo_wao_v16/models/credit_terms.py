from odoo import models, fields

class CreditTerms(models.Model):
    _name = 'credit.terms'
    _description = 'Credit Terms'

    name = fields.Char(string='Name', required=True)
    # Add other fields related to credit terms as needed
