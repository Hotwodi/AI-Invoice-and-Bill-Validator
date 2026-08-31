from odoo import fields, models


class IbvSuspiciousInvoice(models.Model):
    _name = 'ibv.suspicious.invoice'
    _description = 'AI Invoice & Bill Validator - Suspicious Invoice'
    _order = 'ai_risk_score desc, id desc'
    _rec_name = 'name'

    name = fields.Char(string='Reference', required=True)
    invoice_number = fields.Char(string='Invoice Number')
    partner_name = fields.Char(string='Partner')
    amount = fields.Monetary(string='Amount', currency_field='currency_id')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    suspicion_reason = fields.Text(string='Suspicion Reason')
    risk_level = fields.Selection(
        selection=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        string='Risk Level',
        default='low',
        required=True,
    )
    ai_risk_score = fields.Float(
        string='AI Risk Score',
        digits=(5, 2),
        help='AI risk score for this invoice (0.0 to 100.0).',
    )
    state = fields.Selection(
        selection=[
            ('flagged', 'Flagged'),
            ('reviewing', 'Reviewing'),
            ('confirmed', 'Confirmed'),
            ('cleared', 'Cleared'),
        ],
        string='State',
        default='flagged',
        required=True,
    )
    assigned_to = fields.Many2one(
        comodel_name='res.users',
        string='Assigned To',
        default=lambda self: self.env.user,
    )
