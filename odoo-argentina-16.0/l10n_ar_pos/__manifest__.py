# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Argentinean - Point of Sale with AR Doc',
    'version': '1.0',
    'category': 'Accounting/Localizations/Point of Sale',
    'description': """
This module brings the technical requirement for the Argentinean regulation.
Install this if you are using the Point of Sale app in Argentina.
    """,
    'author': 'Odoo, ADHOC SA',

    'depends': [
        'l10n_ar',
        'point_of_sale',
    ],
    'data': [
        'views/template.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'l10n_ar_pos/static/src/**/*'
        ],
    },
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
