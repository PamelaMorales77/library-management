from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Préstamo de libro'

    member_id = fields.Many2one('res.partner', string='Socio', required=True)
    book_id = fields.Many2one('library.book', string='Libro', required=True)

    loan_date = fields.Date(string='Fecha de préstamo', default=fields.Date.today)
    return_date = fields.Date(string='Fecha de devolución')
    due_date = fields.Date(string='Fecha de vencimiento')

    state = fields.Selection([
        ('active', 'Activo'),
        ('returned', 'Devuelto'),
        ('late', 'Vencido'),
    ], default='active', string='Estado')


    def action_return_book(self):
        for record in self:
            record.state = 'returned'
            record.return_date = fields.Date.today()
            record.book_id.state = 'available'

    def action_renew_loan(self):
        for record in self:
            if record.state == 'active':
                record.due_date = fields.Date.today() + timedelta(days=15)


    @api.constrains('book_id', 'member_id', 'state')
    def _check_loan_rules(self):
        for record in self:

            if record.state != 'active':
                continue

            if record.book_id.state != 'available':
                raise ValidationError("El libro no está disponible.")

            loans = self.search([
                ('member_id', '=', record.member_id.id),
                ('state', '=', 'active'),
                ('id', '!=', record.id)
            ])

            if len(loans) >= 5:
                raise ValidationError("El socio ya tiene 5 préstamos activos.")

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record.book_id.state = 'borrowed'
        record.due_date = fields.Date.today() + timedelta(days=30)
        return record


    def check_overdue_loans(self):
        today = fields.Date.today()

        loans = self.search([('state', '=', 'active')])

        for loan in loans:
            if loan.due_date and loan.due_date < today and loan.state != 'late':
                loan.state = 'late'

                if loan.member_id.email:
                    self.env['mail.mail'].create({
                        'subject': 'Préstamo vencido',
                        'body_html': f"""
                            <p>Hola {loan.member_id.name},</p>
                            <p>Tu préstamo del libro <b>{loan.book_id.name}</b> está vencido.</p>
                            <p>Por favor devuélvelo lo antes posible.</p>
                        """,
                        'email_to': loan.member_id.email,
                    }).send()