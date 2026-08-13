# -*- coding: utf-8 -*-

{
    'name': "Automatic Customer Code",
    'version': '1.0',
    'summary': """Unique Customer Code""",
    'description': """Each customer have unique number code""",
    'author': 'Bac Ha Software',
    'company': 'Bac Ha Software',
    'maintainer': 'Bac Ha Software',
    'website': "https://bachasoftware.com",
    'category': 'Sales',
    'depends': ['crm'],
    'data': [
        'views/ir_sequence_data.xml',
        'views/res_partner_form.xml',
        'views/crm_lead_view.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False
}
