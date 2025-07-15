{
  'name': 'Sale Order Delivery Date and Notes',
  'version': '18.0.1.0.0',
  'category': 'Sales',
  'summary': 'Add delivery date and internal notes to sale orders',
  'depends': ['sale'],
  'data': [
    'security/ir.model.access.csv',
    'views/sale_order_views.xml',
  ],
  'installable': True,
  'auto_install': False,
}
