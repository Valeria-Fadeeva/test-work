#!/usr/bin/env python3

import os
import vf_contour as ct


def main(filename, mode=1):
    # путь к файлу с картинкой
    fn = []
    fn.append(os.path.abspath(filename))

    fn.append(os.path.abspath('./images/img.png'))
    fn.append(os.path.abspath('./images/rgb.png'))
    fn.append(os.path.abspath('./images/gray.png'))
    fn.append(os.path.abspath('./images/hsv.png'))
    fn.append(os.path.abspath('./images/tresh.png'))

    ct.color_cvt_save(fn)
    #p = ct.view_figure(fn)
    #p.show()

    fn_list_contours = ct.contour(fn, mode)
    #p = ct.view_figure(fn_list_contours)
    #p.show()

    c = fn + fn_list_contours
    p = ct.view_figure(c)
    p.show()
