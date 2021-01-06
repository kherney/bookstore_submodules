from odoo import fields, models, api


class BookstoreMember(models.Model):
    _inherit = "bookstore.book"

    is_available = fields.Boolean("Is available")
    book_isbn = fields.Char(help="An ISBN is an International Standard Book Number. ISBNs were 10 digits")
    book_publisher = fields.Many2one(index=True)
