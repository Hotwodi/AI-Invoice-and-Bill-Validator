from odoo import fields, models


class IbvValidationSummary(models.Model):
    _name = 'ibv.validation.summary'
    _description = 'AI Invoice & Bill Validator - Validation Summary'
    _order = 'generated_date desc, id desc'
    _rec_name = 'name'

    name = fields.Char(string='Reference', required=True)
    period = fields.Char(string='Period')
    total_invoices = fields.Integer(string='Total Invoices')
    passed = fields.Integer(string='Passed')
    warnings = fields.Integer(string='Warnings')
    errors = fields.Integer(string='Errors')
    ai_accuracy = fields.Float(
        string='AI Accuracy',
        digits=(5, 2),
        help='AI accuracy percentage for this period (0.0 to 100.0).',
    )
    generated_date = fields.Datetime(
        string='Generated Date',
        default=fields.Datetime.now,
    )
