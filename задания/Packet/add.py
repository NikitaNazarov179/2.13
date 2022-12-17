#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add():
    """""
    Запросить данные о продукте.
    """""
    product = input("Название товара: ")
    shop = input("Магазин: ")
    cost = int(input("Стоимость товара: "))

    # Создать словарь
    return {
        'product': product,
        'shop': shop,
        'cost': cost,
    }