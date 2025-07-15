{
  'name': 'CRM Lead Custom Fields with Computed Priority',
  'version': '18.0.1.0.0',
  'category': 'Sales',
  'summary': 'Add custom fields and computed priority to CRM leads',
  'depends': ['crm'],
  'data': [
    'security/ir.model.access.csv',
    'views/crm_lead_views.xml',
  ],
  'installable': True,
  'auto_install': False,
}
