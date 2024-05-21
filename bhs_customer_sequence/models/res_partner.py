# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(string='Customer code', help="The customer code no", default='')

    @api.model
    def create(self, values):
        if values.get('is_company') and not values.get('customer_code'):
            search_partner_mode = self.env.context.get('res_partner_search_mode')
            if search_partner_mode == 'customer' and 'customer_rank' not in values:
                values['customer_rank'] = 1
            seq_customer_code = self.env['ir.sequence'].next_by_code('customer.code')
            if seq_customer_code:
                values['customer_code'] = seq_customer_code
        return super(ResPartner, self).create(values)

    def write(self, vals):
        for partner in self:
            if vals.get('company_type') == 'company' and partner.customer_code == '' and partner.customer_rank > 0:
                seq_customer_code = self.env['ir.sequence'].next_by_code('customer.code')
                if seq_customer_code:
                    vals['customer_code'] = seq_customer_code

            if vals.get('company_type') == 'person':
                vals['customer_code'] = ''

        ret = super(ResPartner, self).write(vals)

        return ret

    @api.depends('complete_name', 'email', 'vat', 'state_id', 'country_id', 'commercial_company_name')
    @api.depends_context('show_address', 'partner_show_db_id', 'address_inline', 'show_email', 'show_vat')
    def _compute_display_name(self):
        super()._compute_display_name()
        for partner in self:
            name = partner.display_name
            if partner.customer_code and partner.customer_rank > 0 and partner.company_type == 'company':
                name = "[%s] %s" % (partner.customer_code, name)

            partner.display_name = name.strip() if name else False

    # def _get_name(self):
    #     name = super(ResPartner, self)._get_name()
    #     if self.customer_code and self.customer_rank > 0 and self.company_type == 'company':
    #         name = "[%s] %s" % (self.customer_code, name)
    #     return name
