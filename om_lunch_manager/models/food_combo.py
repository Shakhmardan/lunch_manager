# -*- coding: utf-8 -*-

from odoo import fields, models


class FoodCombo(models.Model):
    _name = "lunchm.food.combo"
    _description = "Food Combo"

    name = fields.Char(string="Название Меню")
    first_meal = fields.Char(string="Первое блюдо")
    second_meal = fields.Char(string="Второе блюдо")
    apitizer = fields.Char(string="Апитайзер")
    drink = fields.Char(string="Напиток")
    price = fields.Integer(string="Цена")
    cafe_id = fields.Many2one('lunchm.cafe', string="Кафе")
    
    ordered_menu_count = fields.Integer(string="Число заказов", compute='_compute_ordered_menu_count')

    def _compute_ordered_menu_count(self):
        ordered_menu_count = self.env['lunchm.order'].search_count([('combo_id', '=', self.id)])
        self.ordered_menu_count = ordered_menu_count
