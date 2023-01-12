# -*- coding: utf-8 -*-
{
    'name': "FUERZA G3",

    'summary': """
        This application consists in a virtual gym""",

    'description': """
        In the application you can set goals, carry out training and join for
        various events that are organized en diferent places
    """,

    'author': "DAM Tartanga Grupo3",
    'website': "http://www.tartanga.eus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/event.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}