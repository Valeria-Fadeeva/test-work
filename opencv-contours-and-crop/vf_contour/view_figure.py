#!/usr/bin/env python3

import os
import matplotlib.pyplot as plt
import cv2 as cv


def view_figure(fn):
    # Создадим фигуру размером x на y дюйма
    pic_box = plt.figure(figsize=(18, 9))

    l = len(fn)
    h = 2
    w = round(l / h)

    # Поочередно считываем в переменную fn. В переменную i записываем номер итерации
    for i, picture in enumerate(fn):
        # считываем изображение в picture
        picture = cv.imread(picture)
        # конвертируем BGR изображение в RGB
        picture = cv.cvtColor(picture, cv.COLOR_BGR2RGB)
        # добавляем ячейку в pix_box для вывода текущего изображения
        pic_box.add_subplot(h, w, i+1)
        plt.title(os.path.split(fn[i])[-1])
        plt.imshow(picture)
        # отключаем отображение осей
        #plt.axis('off')
    # выводим все созданные фигуры на экран
    #plt.show()
    return plt
