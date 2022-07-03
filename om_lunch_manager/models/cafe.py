# -*- coding: utf-8 -*-

from odoo import api, fields, models


class LunchCafe(models.Model):
    _name = "lunchm.cafe"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Cafe"

    name = fields.Char(string="Название Кафе")
    creator = fields.Char(string="Создатель")
    cafe_type = fields.Char(string="Тип Кафе")
    order_ids = fields.One2many('lunchm.order', 'cafe_id', string="Заказы")
    orders_count = fields.Integer(string="Число заказов", compute='_compute_orders_count')

    def _compute_orders_count(self):
        orders_count = self.env['lunchm.order'].search_count([('cafe_id', '=', self.id)])
        self.orders_count = orders_count

