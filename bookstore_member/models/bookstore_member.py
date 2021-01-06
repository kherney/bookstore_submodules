from odoo import fields, models


class BookstoreMember(models.Model):
    _name = "bookstore.member"
    _description = "Library members"

    member_card_number = fields.Char()
    member_partner_id = fields.Many2one(
        comodel_name="res.partner",
        delegate="True",
        ondelete='cascade',
        required='True',)

