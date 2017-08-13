# -*- coding: utf-8 -*-
{
    'name': "Feitas Academy",

    'summary': """
        Feitas Odoo Dev """,

    'description': """
        Feitas
    """,

    'author': "feitas",
    'website': "http://www.wffeitas.com",

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
        'views/session_views.xml',

        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}