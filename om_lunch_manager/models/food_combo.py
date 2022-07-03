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
