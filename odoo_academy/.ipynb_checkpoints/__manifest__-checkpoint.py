# -*- coding: utf-8 -*- 

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Carlos',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/academy_menuitems.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ]
}