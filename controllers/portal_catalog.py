from odoo import http
from odoo.http import request

class LibraryPortal(http.Controller):

    @http.route(['/my/loans'], type='http', auth="user", website=True)
    def my_loans(self, **kwargs):

        loans = request.env['library.loan'].sudo().search([
            ('member_id', '=', request.env.user.partner_id.id)
        ])

        return request.render('library_management.portal_my_loans', {
            'loans': loans,
        })

    @http.route(['/my/loans'], type='http', auth="user", website=True)
    def my_loans(self, **kwargs):

        loans = request.env['library.loan'].sudo().search([
            ('member_id', '=', request.env.user.partner_id.id)
        ])

        return request.render('library_management.portal_my_loans', {
            'loans': loans,
        })