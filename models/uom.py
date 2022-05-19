# -*- coding: utf-8 -*-
import logging
from odoo import fields, models, api

logger = logging.getLogger()


class UoM(models.Model):
    _inherit = "uom.uom"

    uom_code = fields.Char(
        string="Unit code",
        size=4,
        help="The unit code for 'All-Russian classifier of units of measurement'",
    )
