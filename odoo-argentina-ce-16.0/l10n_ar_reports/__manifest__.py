{
    "name": "Argentinian Reports (CE)",
    "version": "16.0.1.0.0",
    "category": "Localization/Argentina",
    "sequence": 14,
    "author": "ADHOC SA,Moldeo Interactive,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "summary": "",
    "depends": [
        "l10n_ar",
        "report_xlsx",
    ],
    "external_dependencies": {"python": ["xlrd"]},
    "data": [
        "report/account_ar_vat_line_view.xml",
        "report/account_vat_ledger_report.xml",
        "views/account_vat_report_views.xml",
    ],
    "demo": [],
    "images": [],
    'installable': True,
    "auto_install": False,
    "application": False,
}
