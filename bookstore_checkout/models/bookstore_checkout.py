from odoo import models, api, fields


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout"
    _description = "Checkout Request"

    user_id = fields.Many2one(comodel_name="res.users",
                              name="User",
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

    stage_id = fields.Many2one(comodel_name="bookstore.checkout.stage",
                               string="States",
                               default=lambda self: self._default_stage,
                               group_expand="_group_expand_stage_id")
    state = fields.Selection(related="stage_id.state")

    @api.model
    def _default_stage(self):
        stage_env = self.env['bookstore.checkout.stage']
        return stage_env.search([], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)


class BookstoreCheckout(models.Model):
    _name = "bookstore.checkout.line"
    _description = "Checkout Request lines"
    checkout_id = fields.Many2one(comodel_name="bookstore.checkout")
    book_id = fields.Many2one(comodel_name="bookstore.book")
