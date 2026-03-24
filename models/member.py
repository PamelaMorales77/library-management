from odoo import models, fields, api

class LibraryMember(models.Model):
    _inherit = 'res.partner' 

    is_member = fields.Boolean(string="Es socio")
    member_code = fields.Char(string="Código de socio", readonly=True, copy=False)
    member_date = fields.Date(string="Fecha de alta", default=fields.Date.today)

    @api.model
    def _ensure_member_sequence(self):
        seq = self.env['ir.sequence'].search([('code', '=', 'library.member')], limit=1)
        if not seq:
            self.env['ir.sequence'].create({
                'name': 'Código de Socio',
                'code': 'library.member',
                'prefix': 'SOCIO-',
                'padding': 5,
            })

    
    @api.model_create_multi
    def create(self, vals_list):
        self._ensure_member_sequence() 
        for vals in vals_list:
            if vals.get('is_member'):
                vals['member_code'] = self.env['ir.sequence'].next_by_code('library.member') or 'NEW'
        return super().create(vals_list)
    
    
    
     
    def write(self, vals):
        self._ensure_member_sequence()

        res = super().write(vals)

        if 'is_member' in vals:
            for record in self:
                if record.is_member and not record.member_code:
                    record.member_code = self.env['ir.sequence'].next_by_code('library.member')

        return res