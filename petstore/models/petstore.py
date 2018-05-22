# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PetstoreMessage(models.Model):
    _name = "petstore.message"
    _description = 'Message of the day'

    @api.model
    def my_method(self):
        return {"hello": "world"}

    message = fields.Text()
    color = fields.Char(size=20)


class Product(models.Model):
    _inherit = "product.product"

    max_quantity = fields.Float(string="Maximum Quantity")
