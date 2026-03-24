{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Gestión de biblioteca',
    'author': 'Pamela',
    'category': 'Tools',
    'depends': ['base','contacts', 'website', 'portal'],
     'data': [
        'security/security.xml',          
        'security/ir.model.access.csv',
        'views/member_views.xml',
        'views/book_views.xml',
        'views/loan_views.xml',
        'data/cron.xml', 
        'views/portal_catalog.xml',
        'data/portal_data.xml',
    ],

    'installable': True,
    'application': True,
}