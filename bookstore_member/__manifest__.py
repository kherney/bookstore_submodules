{
    'name': 'bookstore_member',
    'version': '13.0.0.1',
    'summary': 'Bookstore extended Module',
    'description': 'Manage people who will be able to borrow books.',
    'author': 'Kevin Herney R.',
    'depends': ['bookstore'],
    'data': [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/bookstore_member_book.xml",
        "views/library_member.xml",
        "views/member_menus.xml",
    ],
    'installable': True,
    'auto_install': False,
    'applications': False,
}
