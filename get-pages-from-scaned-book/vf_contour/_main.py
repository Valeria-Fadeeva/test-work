#!/usr/bin/env python3

import os
import sys
import numpy as np
import cv2 as cv
sys.path.insert(0, '../')
import vf_contour


def main(filename:str, mode:int=2, test:bool=False) -> list:
    filename = os.path.abspath(filename)
    if not os.path.exists(filename):
        raise RuntimeError('{} не найден'.format(filename))

    # чтение изображения
    image = cv.imread(filename)

    im = vf_contour.image_prepare(image)
    if not isinstance(im, np.ndarray):
        raise RuntimeError('Картинки не обработались в файле {}'.format(filename))

    contours = vf_contour.get_contours(im, mode)
    if not isinstance(contours, list) and len(contours) <= 1:
        raise RuntimeError('Контуры не найдены в файле {}'.format(filename))

    images = []
    # цикл по контурам
    for c in contours:
        # аппроксимация (сглаживание) контура
        perimetr = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.02 * perimetr, True)

        img_h, img_w = image.shape[:2]
        x, y, w, h = cv.boundingRect(approx)

        # если у контура 4 вершины, возможно, что это книга
        if w >= (img_w * 0.3) and h >= (img_h * 0.3):
            print('APPROX', len(approx), filename)

            if len(approx) == 4:
                # реализовать проверку на параллелограм
                pass
            
            # если объект занимает больше 30% от ширины и высоты изображения
            # и количество вершин больше, либо равно 3
            elif len(approx) >= 5:
                arr = []
                for g in approx:
                    for hi in g:
                        arr.append([hi[0], hi[1]])

                approx = vf_contour.get_quadrangle_vertices(arr, mode=2)
                #approx = np.array(arr)

            if not isinstance(approx, np.ndarray) and not isinstance(approx, list) and len(approx) <= 1:
                raise RuntimeError('Вершины не получены в файле {}'.format(filename))

            if test:
                rectangle = image.copy()

                cv.drawContours(rectangle, [approx], -1, (0, 255, 0), 4)
                contour_area = cv.contourArea(c)
                text = f"contourArea({c})"
                cv.putText(rectangle, text, (100, 100), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
                text = f"contourArea(c) = {contour_area}"
                cv.putText(rectangle, text, (100, 200), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)

                cv.rectangle(rectangle, (x, y), (x+w, y+h), (0, 255, 255), 2)

                for (x, y) in approx:
                    cv.circle(rectangle, (x, y), 5, (255, 255, 0), -1)
                    text = f"x={x} y={y}"
                    cv.putText(rectangle, text, (x, y), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)

                img = rectangle
                if not isinstance(img, np.ndarray):
                    raise RuntimeError('Картинки не получены в файле {}'.format(filename))
                images.append(img)

            img = vf_contour.image_processing(image, approx, test)
            if not isinstance(img, list):
                raise RuntimeError('Картинки не получены в файле {}'.format(filename))
            images += img

    return images
