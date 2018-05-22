# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Pet Store',
    'version': '1.0',
    'summary': 'Sell pet toys',
    'description':
        """
Odoo Pet Store
=================

A wonderful application to sell pet toys.
        """,
    'category': 'Tools',
    'depends': ['sale_stock'],
    'data': [
        "data/petstore_data.xml",
        "data/petstore.message.csv",
        "views/petstore_views.xml",
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}
