{
    'name': 'AI Invoice & Bill Validator',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'AI-powered validation of invoices and bills with rule-based checks and risk scoring.',
    'description': """
AI Invoice & Bill Validator
============================
Validate invoices and bills automatically using configurable rules and AI-driven
risk scoring. Detect duplicate invoices, amount mismatches, tax anomalies,
suspicious vendors, and more. Review suspicious invoices, track validation
results, and generate period summaries to keep your accounts clean.
""",
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 49.99,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/ibv_validation_rule_views.xml',
        'views/ibv_validation_result_views.xml',
        'views/ibv_suspicious_invoice_views.xml',
        'views/ibv_validation_summary_views.xml',
        'views/ibv_menu.xml',
    ],
}
