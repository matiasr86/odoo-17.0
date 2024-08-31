{
    "name": "Factura Electrónica Argentina",
    "version": "16.0.2.0.0",
    "category": "Localization/Argentina",
    "sequence": 14,
    "author": "ADHOC SA, Moldeo Interactive,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "summary": "",
    "depends": [
        "l10n_ar_afipws",
        "l10n_ar",
        "account_debit_note",
    ],
    "external_dependencies": {},
    "data": [
        "views/account_move_views.xml",
        "views/account_journal_view.xml",
        "views/report_invoice.xml",
        "views/res_config_settings.xml",
        "views/menuitem.xml",
        "views/ir_cron.xml",
        "wizard/account_validate_account_move.xml",
    ],
    "demo": [],
    "images": [],
    'installable': True,
    "auto_install": False,
    "application": False,
}