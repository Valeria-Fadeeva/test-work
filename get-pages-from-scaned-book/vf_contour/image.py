#!/usr/bin/env python3

import numpy as np
import cv2 as cv
from imutils import perspective
from math import floor

def image_prepare(image):
    if (len(image.shape) < 3):
        gray = image
    elif len(image.shape) == 3:
        # смена цветовой модели с BGR на GRAY scale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        raise RuntimeError('Странное цветовое пространство')

    #canvas = np.zeros(image.shape, np.uint8)
    # filter out small lines
    #kernel = np.ones((5, 5), np.float32)/25
    #gray = cv.filter2D(gray, -1, kernel)

    # уменьшение резкости
    gray = cv.GaussianBlur(gray, (3, 3), 0)

    # распознавание контуров
    edged = cv.Canny(gray, 10, 250)
    #edges = cv.Canny(gray, 100, 200)

    # создание закрывающих контуров
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    closed = cv.morphologyEx(edged, cv.MORPH_CLOSE, kernel)

    # создание черно-белого изображения
    _, binary = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

    image = binary
    
    return image


def image_processing(image, approx, test:bool=False):
    images = []

    x, y, w, h = cv.boundingRect(approx)

    rectangle = image
    cv.rectangle(rectangle, (x, y), (x+w, y+h), (0, 255, 255), 2)
    if test:
        text = f"rectangle"
        cv.putText(rectangle, text, (100, 300), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
        images.append(rectangle)
    
    rect = cv.minAreaRect(approx)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    pts = np.array(box)

    if test:
        circle = rectangle
        for (x, y) in pts:
            cv.circle(circle, (x, y), 5, (0, 255, 0), -1)
        text = f"circle"
        cv.putText(circle, text, (100, 400), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
        images.append(circle)

    # разворот изображения в положение паралельно плоскостям X и Y
    if test:
        warped = perspective.four_point_transform(circle, pts)
    else:
        warped = perspective.four_point_transform(rectangle, pts)

    if test:
        text = f"warped"
        cv.putText(warped, text, (100, 500), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
        images.append(warped)

    h, w = warped.shape[:2]
    x = 0
    y = 0

    # 1.5 процента для обрезки
    margin = 0.015

    # обрезка изображения с вычитанием % от ширины и высоты
    crop_img = warped[
        y + floor(h * margin): y + h - floor(h * margin),
        x + floor(w * margin): x + w - floor(w * margin)
    ]

    h, w = crop_img.shape[:2]

    ci = False
    if h >= w:
        images.append(crop_img)
        ci = True
    elif w > h:
        # вычитание из изображения правой части
        left_img = crop_img[
            y: y + h,
            x: x + floor(w/2) - floor(w * margin)
        ]
        if test:
            text = f"left_img"
            cv.putText(left_img, text, (100, 600), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
        images.append(left_img)

        # вычитание из изображения левой части
        right_img = crop_img[
            y: y + h,
            floor(w/2) + floor(w * margin): w
        ]
        if test:
            text = f"right_img"
            cv.putText(right_img, text, (100,600), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
        images.append(right_img)

    if test and ci == False:
        text = f"crop_img"
        cv.putText(crop_img, text, (100, 500), cv.FONT_HERSHEY_DUPLEX, 2, (100, 100, 100), 8)
        images.append(crop_img)

    return images
