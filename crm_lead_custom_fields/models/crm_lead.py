from odoo import models, fields, api
import random


class CrmLead(models.Model):
  _inherit = 'crm.lead'

  source = fields.Char('Source')
  priority = fields.Selection([
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
  ], string='Priority', default='medium')
  tags = fields.Many2many('crm.tag', string='Tags')
  computed_attention_priority = fields.Char(string='Computed Attention Priority', compute='_compute_attention_priority', store=False)

  @api.depends('priority')
  def _compute_attention_priority(self):
    for record in self:
      record.computed_attention_priority = random.choice(['High', 'Medium', 'Low'])
