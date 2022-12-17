#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list(products):
    """""
    Отобразить список работников
    """""
    # Проверить что список работников не пуст
    if products:
        # Заголовок таблицы
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Товар",
                "Магазин",
                "Стоимость товара"
            )
        )
        print(line)

        for idx, products in enumerate(products, 1):
            print(
                '| {:^4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    products.get('product', ''),
                    products.get('shop', ''),
                    products.get('cost', ''),
                    ' ' * 5
                )
            )

        print(line)

    else:
        print("Список товаров пуст.")