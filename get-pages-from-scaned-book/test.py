#!/usr/bin/env python3

import os
import sys
import argparse
import cv2 as cv
import vf_contour


def main():
    c = sys.argv[0]
    fname = os.path.split(c)[-1]
    p = c.replace(fname, '')

    source_dir = os.path.abspath(os.path.join(p, 'images'))
    result_dir = os.path.abspath(os.path.join(p, 'test'))

    filename = 'i007_big.png'
    img_p = os.path.join(source_dir, filename)

    fso_start_format = [img_p]

    subproject_result_path = result_dir

    mode = 1
    '''
    cv2.RETR_LIST       → Retrieve all contours
    cv2.RETR_EXTERNAL   → Retrieves external or outer contours only
    cv2.RETR_CCOMP      → Retrieves all in a 2-level hierarchy
    cv2.RETR_TREE       → Retrieves all in the full hierarchy
    '''

    """получить из отсканированных изображений обработанные и сохранить в результирующую папку"""
    i = 0
    for f in fso_start_format:
        fname = os.path.split(f)[-1]
        fn = os.path.splitext(fname)[0]
        ext = os.path.splitext(fname)[-1]
        dig = vf_contour.get_cnt_num_from_string(vf_contour.str_to_int(fn))
        if not dig:
            raise RuntimeError('Цифры не найдены в имени файла {}'.format(f))

        img_list = vf_contour.main(f, mode=mode, test=True)
        if not img_list:
            raise RuntimeError('Картинки не обработались в файле {}'.format(f))
            
        for img in img_list:
            fname = '{:{fill}{align}{width}}'.format(i, fill=0, align='>', width=dig) + ext
            res_f = os.path.join(subproject_result_path, fname)
            cv.imwrite(res_f, img)
            print(i, f, '=>', res_f)

            i += 1

if __name__ == '__main__':
    main()
