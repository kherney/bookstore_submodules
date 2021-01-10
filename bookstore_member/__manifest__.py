{
    'name': 'bookstore_member',
    'version': '13.0.1.0',
    'summary': 'Bookstore extended Module',
    'description': 'Manage people who will be able to borrow books.',
    'author': 'Kevin Herney R.',
    'depends': ['bookstore', 'mail'],
    'data': [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/bookstore_member_book.xml",
        "views/library_member.xml",
        "views/bookstore_book_list_inherit.xml",
        "views/member_menus.xml",
    ],
    'installable': True,
    'auto_install': False,
    'applications': False,
}
