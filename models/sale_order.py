from odoo import models, fields


class SaleOrder(models.Model):
  _inherit = 'sale.order'

  delivery_date = fields.Date('Delivery Date')
  internal_notes = fields.Text('Internal Notes')
