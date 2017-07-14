# -*- coding: utf-8 -*-
{
    'name' : 'MH :: Analysis Report',
    'version' : '1.0',
    'author' : 'Ecosoft',
    'category' : 'Sales',
    'description' : """

* Sales / Invoice Analysis

    """,
    'website': 'www.ecosoft.co.th',
    'depends' : [
        'materialized_sql_view',
    ],
    'data': [
        'materialized_view_data.xml',
        'mh_invoice_analysis_report_view.xml'
    ],
    'qweb' : [
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
