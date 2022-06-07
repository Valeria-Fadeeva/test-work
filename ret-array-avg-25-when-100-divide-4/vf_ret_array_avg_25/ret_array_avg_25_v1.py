#!/usr/bin/env python3

from typing import List
from random import randrange


def ret_array_avg_25_v1(mass: int, size: int, verbose: bool = False) -> List[int]:
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

    # 15
    mid: int = round((s_40 - s_10) / 2)

    # 25
    mid_seq: int = s_10 + mid

    # 24
    left_seq: int = mid_seq - 1

    # 25
    right_seq: int = mid_seq

    # массив значений
    arr: List[int] = []

    # желаемое направление
    wish_way: bool = False

    for i in range(size):
        # сумма заполненных чисел
        summa_chisel: int = sum(arr)

        # если это первый элемент
        if wish_way == False:
            # взять рандомное число с 10 по 40
            r: int = randrange(s_10, s_40, 1)

        # иначе если желаемое направление слева от центра (24)
        elif wish_way == 'left':
            # взять рандомное число с 10 по 24 (25)
            # если необходимо, чтобы чаще попадало число, близкое к центру, то добавляем 1
            r: int = randrange(s_10, left_seq+1, 1)

        # иначе если желаемое направление справа от центра (25)
        elif wish_way == 'right':
            # взять рандомное число с 25 (24) по 40
            # если необходимо, чтобы чаще попадало число, близкое к центру, то вычитаем 1
            r: int = randrange(right_seq-1, s_40, 1)

        # если число больше 25
        if r > mid_seq:
            # желаемое направление - 10 - 24
            wish_way: str = 'left'

        # если число меньше, либо равно 25
        elif r <= mid_seq:
            # желаемое направление - 25 - 40
            wish_way: str = 'right'

        # если осталось 2 незаполненных элемента
        if len(arr) == size / 2:
            # если сумма чисел меньше 50
            if summa_chisel < mass / 2:
                # если сумма чисел равна 20
                if summa_chisel == s_10 + s_10:
                    # число равно 40
                    r: int = s_40
                # иначе
                else:
                    # число равно от (100 - сумма 2 чисел - 40) до 40
                    r: int = randrange(mass - summa_chisel - s_40, s_40, 1)
            # если сумма чисел больше, либо равна 50
            elif summa_chisel >= mass / 2:
                # если сумма чисел равна 80
                if summa_chisel == s_40 + s_40:
                    # число равно 10
                    r: int = s_10
                # иначе
                else:
                    # число равно от 10 до (100 - сумма 2 чисел - 10)
                    r: int = randrange(s_10, mass - summa_chisel - s_10, 1)

        # если остался только 1 незаполненный элемент
        elif size - len(arr) == 1:
            r: int = mass - summa_chisel

        # добавить число в массив
        arr.append(r)

        # остаток от вычитания (диагностика)
        lap: int = mass - sum(arr)

        if verbose:
            print('mass - sum({}) = '.format(arr), lap, end='\n\n')

    return arr
