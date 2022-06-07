#!/usr/bin/env python3

import vf_ret_array_avg_25
from typing import List
import argparse


def main(verbose: bool = False, ver: int = 2) -> None:
    block_separator: str = '=' * 20

    result: List[List[int]] = []

    cnt3: List[int] = []
    cnt4: List[int] = []

    mass: int = 100
    size: int = 4

    # запустить 1 000 000 раз
    cnt_run: int = 1000000
    if ver == 1:
        for i in range(cnt_run):
            result.append(vf_ret_array_avg_25.ret_array_avg_25_v1(mass, size, verbose))
    elif ver == 2:
        for i in range(cnt_run):
            result.append(vf_ret_array_avg_25.ret_array_avg_25_v2(mass, size, verbose))

    if result:
        for i in range(len(result)):
            
            k: int = 0
            
            for j in result[i]:
                if j in [24,25]:
                    k += 1
                    
                    if k == 3:
                        cnt3.append(i)
                    
                    elif k == 4:
                        cnt4.append(i)

        # подсчитать количество ячек, где числа в диапазоне 24..25
        if verbose:
            for z in cnt3: 
                print(result[z])

            print(block_separator)

            for x in cnt4:
                print(result[x])
        
        #print(cnt3)
        print('У {} из {} 3 значения находятся в диапазоне 24..25'.format(
            len(cnt3), cnt_run))

        print(block_separator)

        #print(cnt4)
        print('У {} из {} 4 значения находятся в диапазоне 24..25'.format(
            len(cnt4), cnt_run))
    else:
        raise RuntimeError('Пустое значение result')

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
