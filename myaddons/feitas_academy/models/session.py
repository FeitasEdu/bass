# -*- coding: utf-8 -*-

from odoo import models, fields, api

class faSession(models.Model):
    _name = 'fa.session'

    name = fields.Char(string="班次")
