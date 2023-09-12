# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Bravo custom module",
    'version': '16.0.1.0.0',
    'summary': """Added extra fields to run the flow""",
    "category": 'Extra Tools',
    'description': """Added extra fields to run the flow""",
    'author': 'Wao connect- Dev Team',
    'company': 'Wao Connect',
    'maintainer': 'Wao connect',
    'website': 'https://www.waoconnect.com',
    'depends': ['base', 'contacts' , 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/bravo_customer_views.xml',
        'views/bravo_spplier_views.xml',
      #  'views/credit_term_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'demo': [

    ],
    'installable': True,

}
