#!/usr/bin/env python3

import cv2 as cv
import numpy as np


def color_cvt_save(fn):
    frame = cv.imread(fn[0])

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    (h, s, v) = cv.split(hsv)
    v[:] = 100
    img = cv.merge((v, v, s))
    cv.imwrite(fn[1], img)

    rgb = cv.cvtColor(img, cv.COLOR_HSV2RGB)
    cv.imwrite(fn[2], rgb)

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imwrite(fn[3], gray)
    
    # параметры цветового фильтра
    hsv_min = np.array((2, 28, 65), np.uint8)
    hsv_max = np.array((26, 238, 255), np.uint8)
    
    # меняем цветовую модель с BGR на HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imwrite(fn[4], hsv)
    
    # применяем цветовой фильтр
    thresh = cv.inRange(hsv, hsv_min, hsv_max)
    cv.imwrite(fn[5], thresh)
    
    return True
