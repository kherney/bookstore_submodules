from odoo import fields, models, api


class BookstoreMember(models.Model):
    _inherit = "bookstore.book"

    is_available = fields.Boolean("Is available")
    book_isbn = fields.Char(help="An ISBN is an International Standard Book Number. ISBNs were 10 digits")
    book_publisher = fields.Many2one(index=True)

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.book_isbn if x.isdigit()]
        if len(digits) == 10:
            ponderators = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            total = sum(a * b for a, b in zip(digits[:9], ponderators))
            check = total % 11
            return digits[-1] == check
        else:
            return super()._check_isbn()
