from odoo import api, fields, models


class IbvValidationRule(models.Model):
    _name = 'ibv.validation.rule'
    _description = 'AI Invoice & Bill Validator - Validation Rule'
    _order = 'sequence, name'
    _rec_name = 'name'

    name = fields.Char(string='Rule Name', required=True, translate=True)
    sequence = fields.Integer(string='Sequence', default=10)
    rule_type = fields.Selection(
        selection=[
            ('amount_match', 'Amount Match'),
            ('tax_check', 'Tax Check'),
            ('duplicate_invoice', 'Duplicate Invoice'),
            ('vendor_verify', 'Vendor Verify'),
            ('date_check', 'Date Check'),
            ('round_number', 'Round Number'),
        ],
        string='Rule Type',
        required=True,
        default='amount_match',
    )
    field_name = fields.Char(
        string='Target Field',
        help='Technical name of the invoice field this rule inspects.',
    )
    condition = fields.Text(
        string='Condition',
        help='Condition expression or description evaluated by this rule.',
    )
    severity = fields.Selection(
        selection=[
            ('warning', 'Warning'),
            ('error', 'Error'),
        ],
        string='Severity',
        required=True,
        default='warning',
    )
    active = fields.Boolean(string='Active', default=True)
    violations_found = fields.Integer(
        string='Violations Found',
        compute='_compute_violations_found',
        store=True,
        help='Number of validation results flagged by this rule.',
    )

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The rule name must be unique.'),
    ]

    @api.depends('name')
    def _compute_violations_found(self):
        Result = self.env['ibv.validation.result']
        for rule in self:
            rule.violations_found = Result.search_count([
                ('rule_id', '=', rule.id),
                ('result', 'in', ['warning', 'error']),
            ])
