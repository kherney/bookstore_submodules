from odoo import fields, models, api


class BookstoreMember(models.Model):
    _inherit = "bookstore.book"

    is_available = fields.Boolean("Is available")
