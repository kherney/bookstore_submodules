{
    'name': 'bookstore_checkout',
    'description': 'members can borrow their books',
    'author': 'Kherney',
    'depends': ['bookstore'],
    'data': [
        'security/ir.model.access.csv',
        'views/checkout_menu.xml',
        'views/checkout_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
