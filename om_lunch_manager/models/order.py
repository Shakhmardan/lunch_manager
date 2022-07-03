# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Order(models.Model):
    _name = "lunchm.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Order"

    name = fields.Char(string="Имя")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Пол")
    cafe_id = fields.Many2one('lunchm.cafe', string="Кафе")
    combo_id = fields.Many2one('lunchm.food.combo', string="Меню")

    @api.onchange('cafe_id')
    def onchange_cafe_id(self):
        for rec in self:
            return {'domain': {'combo_id': [('cafe_id', '=', rec.cafe_id.id)]}}
