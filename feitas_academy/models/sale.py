# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api


_logger = logging.getLogger(__name__)


class AcademySaleOrder(models.Model):
    _inherit = "sale.order"

    test_char = fields.Char(string="测试字段Char")
