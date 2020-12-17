# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.


{
    'name': 'Employee Expense Tripple Approval',
    'version': '1.4',
    'price': 52.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'category': 'Human Resources',
    'summary': 'This app set workflow tripple approval on expense submitted by Employees.',
    'description': """
Employee expense
expense
Employee Expense Tripple Approval
hr expense
hr expense workflow
expense approval
expense employee approve
expense employee approval
human resource expense app
expense app
odoo expense
expense odoo
expense workflow in odoo
hr expense expense
expense sheet approve
expense sheet approval
employee expense sheet approval
expense flow
expense print
print expense
expense management
expense odoo
expense department
department expense
finaince expense
expense accounting
expense cost
expense financial approval
expense data
expense sheet
expense submit
submit expense
submit expense sheet
approve expense
expense approve accounting
expense costing
expense sheet user
user expense
quick expense
tripple approval
double approval
expense tripple approval
expense double approval
expense approval workflow
allow approval expense
submittion expense
employee submit expense
openerp expense
detail expense
expense picture

    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpeg'],
    'live_test_url': 'https://youtu.be/sV1GGihdyMo',
#    'live_test_url': 'https://youtu.be/bEQRNUWzvGg',
    'depends': [
        'hr_expense',
        'ja_expense_overview',
    ],
    'data': [
        'security/hr_expense_security.xml',
        'views/hr_expense_sheet_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
