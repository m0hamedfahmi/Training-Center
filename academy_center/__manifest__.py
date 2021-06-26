# -*- coding: utf-8 -*-
{
    'name': "Academy Center",

    'summary': """
        The Academy Center of the Arts is Lynchburg, Virginia's center for arts, culture, and community building.
         Our mission is to serve our community through arts """,

    'description': """
        Long description of module's purpose
    """,

    'author': "M.Fahmi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
