from odoo import models, api, fields


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout"
    _description = "Checkout Request"

    user_id = fields.Many2one(comodel_name="res.users",
                              name="Librarian",
                              default=2,
                              readonly=True)
    member_book_id = fields.Many2one("bookstore.member",
                                     string="Librarian",
                                     required=True)
    request_date = fields.Date(
        default=lambda s: fields.Date.today())

    line_ids = fields.One2many("bookstore.checkout.line",
                               "checkout_id",
                               string="Borrowed Books")


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout.line"
    _description = "Checkout Request lines"
    checkout_id = fields.Many2one(comodel_name="bookstore.checkout")
    book_id = fields.Many2one(comodel_name="bookstore.book")

