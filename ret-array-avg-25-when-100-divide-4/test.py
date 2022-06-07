#!/usr/bin/env python3

import argparse
import vf_ret_array_avg_25
from typing import List, Callable
from termcolor import colored
from colorama import init
init()


def test_ret_array_avg_25(f: Callable[[int, int], List[int]], mass: int, size: int, verbose: bool = False) -> int:
    """Функция тестирования
    
    Keyword arguments:
    f -- Функция, которую будем тестировать
    Return: Статус типа int
    """

    result: List[int] = f(mass, size, verbose)

    if len(result) == 4:
        pass
    else:
        # проверка, что список содержит 4 элемента
        if verbose:
            text: str = 'ERROR: return list length != {}'.format(size)
            print(colored(text, 'red', 'on_white'))
        
        ret: int = 1

    for i in result:
        if i >= 10 and i <= 40:
            pass
        else:
            # проверка, что числа в списке не выходят за границы 10 .. 40
            if verbose:
                text: str = 'ERROR: value in result list out of range 10 .. 40: {}'.format(i)
                print(colored(text, 'red', 'on_white'))
            
            ret: int = 2

    if verbose:
        text: str = 'PASS'
        print(colored(text, 'green', 'on_white'))

    if 'ret' not in locals():
        ret: int = 0

    return ret


def main(verbose: bool = False, ver: int = 2) -> None:
    n: int = 1000
    a: int = 0
    b: int = 0
    c: int = 0

    block_separator: str = '=' * 20
    mass: int = 100
    size: int = 4

    if ver == 1:
        for i in range(n):
            status: int = test_ret_array_avg_25(vf_ret_array_avg_25.ret_array_avg_25_v1, mass, size, verbose)

            if status == 0:
                a += 1

            elif status == 1:
                b += 1

            elif status == 2:
                c += 1
    
    elif ver == 2:
        for i in range(n):
            status: int = test_ret_array_avg_25(vf_ret_array_avg_25.ret_array_avg_25_v2, mass, size, verbose)

            if status == 0:
                a += 1

            elif status == 1:
                b += 1

            elif status == 2:
                c += 1

    print()
    print(block_separator)
    print('Успешно завершено', a, 'тестов из', n)
    print('Провалено тестов ', b, 'с ошибкой типа "return list length != 4"')
    print('Провалено тестов ', c, 'с ошибкой типа "value in result list out of range 10 .. 40"')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Программа: делит число 100 на 4 части случайного размера при этом чтобы каждое число было от 10 до 40",
        epilog='Используйте %(prog)s {command} -h для справки о командах')
    parser.add_argument('-v', '--version', action='version', version=' (%(prog)s) ' + vf_ret_array_avg_25.copyright)
    parser.add_argument('-V', '--verbose', help='verbose mode', action="store_true")
    parser.add_argument('-c', type=int, help='version of command')
    args = parser.parse_args()

    if args.c == None:
        ver: int = 2
    elif isinstance(args.c, int) and args.c >= 1 and args.c <= 2:
        ver: int = args.c

    main(verbose=args.verbose, ver=ver)
