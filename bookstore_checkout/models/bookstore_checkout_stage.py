from odoo import models, fields


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout.stage"
    _description = "Checkout Stage"
    _order = "state"

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean(default=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'),
                   ('open', 'Open'),
                   ('done', 'Done'),
                   ('cancel', 'Cancel'), ],
        required=False,
        default="new")
