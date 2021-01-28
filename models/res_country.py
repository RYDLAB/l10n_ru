# -*- coding: utf-8 -*-

from odoo import fields, models


class Country(models.Model):
    _inherit = "res.country"

    number_code = fields.Char(string="Number code", size=3)


class CountryState(models.Model):
    _inherit = "res.country.state"

    number_code = fields.Char(string="Number code", size=3)
