# -*- coding: utf-8 -*-
{
    'name': "Clinica",

    'summary': """
        Módulo para la gestión de pacientes de un clínica""",

    'description': """
        Gestión de pacientes de una clinica
    """,

    'author': "aaparicio",
    'website': "http://www.myclinica.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/clinica_security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/vista_pacientes.xml',
        'views/vista_historial.xml',
        'views/vista_producto.xml',
        'views/vista_menu.xml',
            
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'application': True,
    'installable': True,

}