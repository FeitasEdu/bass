# -*- coding: utf-8 -*-
{
    'name': "feitasacademy",

    'summary': """
        Feitas Odoo Dev """,

    'description': """
        Just A Test Model ！
    """,

    'author': "Feitas Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Feitas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}