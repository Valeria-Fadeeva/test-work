#!/usr/bin/env python3

from typing import List
from random import randrange
from math import floor


def ret_array_avg_25_v2(mass: int, size: int, verbose: bool = False) -> List[int]:
    """Функция делит число 100 на 4 части случайного размера при этом чтобы каждое число было от 10 до 40
    
    Keyword arguments:
    mass -- Число, которое нужно поделить;
    size -- Число, частей, которые нужно получить
    Return: Список значений
    """

    # начальное значение
    s_10: int = 10

    # конечное значение
    s_40: int = 40

    # массив значений
    arr: List[int] = []

    for i in range(size):
        # сумма заполненных чисел
        summa_chisel: int = sum(arr)

        # если это первый элемент
        if len(arr) == 0:
            # взять рандомное число с 10 по 40
            r: int = randrange(s_10, s_40, 1)

        # если это второй элемент
        elif len(arr) == 1:
            # взять округленное число, полеченное делением остатка от вычитания первого числа, деленного на 3
            r: int = floor((mass - summa_chisel) / 3)

        # если это третий элемент
        elif len(arr) == 2:
            # взять округленное число, полеченное делением остатка от вычитания первого числа, деленного на 3
            pass

        # если это последний элемент
        elif len(arr) == 3:
            r: int = mass - summa_chisel

        # добавить число в массив
        arr.append(r)

        # остаток от вычитания (диагностика)
        lap: int = mass - sum(arr)

        if verbose:
            print('mass - sum({}) = '.format(arr), lap, end='\n\n')

    return arr
