# -*- coding: utf-8 -*-
{
    'name': 'Lunch Management',
    'version': '1.0.0',
    'category': 'Lunch',
    'summary': 'Lunch Management System',
    'description': """Lunch Management System""",
    'author': 'Shakh',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/cafes_view.xml',
        'views/order_view.xml',
        'views/food_combo_view.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
