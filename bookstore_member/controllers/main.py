from odoo.addons.bookstore.controllers.main import Bookstore
from odoo import http


class BooksExtended(Bookstore):

    @http.route()
    def list_books(self, **kwargs):
        response = super().list_books(**kwargs)
        if kwargs.get('available'):
            book_rqst = http.request.env['bookstore.book']
            book_records = book_rqst.search([('is_available', '=', True)])
            response.qcontext['book_recordset'] = book_records
        return response
