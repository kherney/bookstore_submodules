from odoo import models, api, fields


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout"
    _description = "Checkout Request"

    member_id = fields.Many2one(comodel="bookstore.member", required=True)
    user_id = fields.Many2one(comodel="res.user",
                              name="Librarìan",
                              default=lambda s: fields.env.uid)
    request_date = fields.Date(
        default=lambda s: fields.Date.today())

    line_ids = fields.One2many("bookstore.checkout.line",
                               "checkout_id",
                               string="Borrowed Books")


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout.line"
    _description = "Checkout Request lines"
    checkout_id = fields.Many2one(comodel="bookstore.checkout")
    book_id = fields.Many2one(comodel="bookstore.book")

