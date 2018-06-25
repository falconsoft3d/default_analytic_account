# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Cuentas Analíticas por defecto",
    'summary': """Carga Cuentas Analíticas por defecto al crear un documento""",
    'description': """
        Agrega campo Cuenta Analítica en Productos y Partner.
    """,
    'author': "Falcón Solutions",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Account',
    'version': '10.0.1',
    'depends': ['analytic','sale','purchase','account'],
    'data': [
        'views/product_view.xml',
        'views/partner_view.xml',
    ],
    'demo': [
    ],
}
