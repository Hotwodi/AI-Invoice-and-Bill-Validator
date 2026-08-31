from odoo import fields, models


class IbvValidationResult(models.Model):
    _name = 'ibv.validation.result'
    _description = 'AI Invoice & Bill Validator - Validation Result'
    _order = 'detected_date desc, id desc'
    _rec_name = 'name'

    name = fields.Char(string='Reference', required=True)
    invoice_ref = fields.Char(string='Invoice Reference')
    partner_name = fields.Char(string='Partner')
    amount = fields.Monetary(string='Amount', currency_field='currency_id')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    rule_id = fields.Many2one(
        comodel_name='ibv.validation.rule',
        string='Validation Rule',
        ondelete='restrict',
    )
    result = fields.Selection(
        selection=[
            ('pass', 'Pass'),
            ('warning', 'Warning'),
            ('error', 'Error'),
        ],
        string='Result',
        required=True,
        default='pass',
    )
    ai_confidence = fields.Float(
        string='AI Confidence',
        digits=(5, 2),
        help='AI confidence score for this result (0.0 to 100.0).',
    )
    message = fields.Text(string='Message')
    detected_date = fields.Datetime(
        string='Detected Date',
        default=fields.Datetime.now,
    )
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('resolved', 'Resolved'),
            ('ignored', 'Ignored'),
        ],
        string='State',
        default='new',
        required=True,
    )
