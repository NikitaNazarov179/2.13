#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select(products, addedtovar):
    """""
    Выбрать необходимый товар
    """""
    result = [product for product in products if product.get('product', '') == addedtovar]
    return result