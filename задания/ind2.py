#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from Packet.add import add
from Packet.list import list
from Packet.select import select
from Packet.help_1 import help_1


def main():
    """""
    Главная функция программы
    """""
    print("help - список всех команд")
    # Список товаров
    products = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = add()
            products.append(product)

            if len(products) > 1:
                products.sort(key=lambda d: d.get('product', ''))

        elif command == 'list':
            list(products)

        elif command == 'select':
            print("Введите товар, информацию о котором хотите получить: ")
            tov = input()
            selected = select_product(products, tov)
            select(selected)

        elif command == 'help':
            help_1()

        else:
            print(f"Неизвестная комманда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()