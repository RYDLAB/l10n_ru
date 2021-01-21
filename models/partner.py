# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    psrn = fields.Char(
        string="PSRN", help="Primary State Registration Number", index=True
    )
    iec = fields.Char(
        string="IEC", help="Industrial Enterprises Classifier", index=True
    )
    okpo = fields.Char(
        string="OKPO",
        help="All-Russian Classifier of Enterprises and Organizations",
        index=True,
    )
    passport_number = fields.Char(
        string="Passport №", help="Passport series and number", index=True
    )
    passport_department = fields.Char(
        string="Passport issued by", help="Department issued the passport"
    )
    passport_date = fields.Date(
        string="Passport issue date", help="Passport's date of issue"
    )
