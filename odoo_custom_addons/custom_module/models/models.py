# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_module(models.Model):
    _name = 'custom_module.custom_module'
    _description = 'Medicines Model'

    name = fields.Char()
    description = fields.Text()
    usage_type = fields.Char()
    barcode = fields.Char()
    sale_price = fields.Float()
    scientific_name = fields.Char()
    originator = fields.Char(string="Company")
    moves = fields.One2many(
        comodel_name="custom_module.moves", inverse_name='medicine')
    quantity_available = fields.Float(compute="_get_quantity", store=True)

    def _get_quantity(self):
        for record in self:
            record.quantity_available = sum(record.moves.mapped('quantity'))

    # quantity_available = fields.Float(compute='_get_quantity', store=True)

    # def _get_quantity(self):
    #     for record in self:
    #         record.quantity_available = sum(record.moves.mapped('quantity'))


class MedicinesMove(models.Model):
    _name = 'custom_module.moves'
    _description = 'Medicines Moves'

    name = fields.Char()
    quantity = fields.Float()
    timestamp = fields.Datetime()
    medicine = fields.Many2one(comodel_name='custom_module.custom_module')
