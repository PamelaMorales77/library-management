from odoo import models, fields, api
from datetime import date

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro de la biblioteca'

    image = fields.Binary(string='Portada', attachment=True)
    
    name = fields.Char(string='Título', required=True)
    author = fields.Char(string='Autor')
    isbn = fields.Char(string='ISBN')
    publication_year = fields.Integer(string='Año de publicación')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('borrowed', 'Prestado'),
        ('lost', 'Perdido'),
    ], string='Estado', default='available')
    
    years_since_publication = fields.Integer(
        string='Años desde publicación', compute='_compute_years_since_publication', store=True
    )

    @api.depends('publication_year')
    def _compute_years_since_publication(self):
        for book in self:
            if book.publication_year:
                book.years_since_publication = date.today().year - book.publication_year
            else:
                book.years_since_publication = 0