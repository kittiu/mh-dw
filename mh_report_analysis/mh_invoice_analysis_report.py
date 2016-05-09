# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import tools
import openerp.addons.decimal_precision as dp
from openerp import fields, models


class MHInvoiceAnalysisReport(models.Model):

    _name = 'mh.invoice.analysis.report'
    _auto = False
    _rec_name = 'day'

    _inherit = [
        'abstract.materialized.sql.view',
    ]

    id = fields.Integer(string='ID')
    date = fields.Date(string='Date')
    year = fields.Char(string='Year')
    month = fields.Char(string='Month')
    day = fields.Char(string='Date')
    type = fields.Selection(
        [('out_invoice', 'Customer Invoice'),
         ('in_invoice', 'Supplier Invoice'),
         ('out_refund', 'Customer Refund'),
         ('in_refund', 'Supplier Refund'),
         ], string='Type')
    state = fields.Selection(
        [('draft', 'Draft'),
         ('proforma', 'Pro-forma'),
         ('proforma2', 'Pro-forma'),
         ('open', 'Open'),
         ('paid', 'Done'),
         ('cancel', 'Cancelled'),
         ], string='Status')
    partner_code = fields.Char(string='Customer Code')
    cust_name = fields.Char(string='Customer Name')
    cust_so_name = fields.Char(string='Customer SO Name')
    product_code = fields.Char(string='Product Code')
    product_full_name = fields.Char(string='Product Name')
    product_qty = fields.Float(string='Product Quantity')
    uom_name = fields.Char(string='Unit of Measure')
    price_average = fields.Float(string='Average Price')
    price_total = fields.Float(string='Total')
    product_category = fields.Char(string='Product Category')
    sale_person = fields.Char(string='Salesperson')
    #_order = 'id, date desc'

    _sql_view_definition = """
        select * from mh_invoice_analysis_dw
    """

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
