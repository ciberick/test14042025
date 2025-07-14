from odoo import models, fields


class CrmLead(models.Model):
  _inherit = 'crm.lead'

  source = fields.Char('Source')
  priority = fields.Selection([
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
  ], string='Priority', default='medium')
  tags = fields.Many2many('crm.tag', string='Tags')
