#!/usr/bin/env python3

import os
import cv2 as cv


def contour(fn, mode=1):
    fn_result_list = []
    
    NEXT_SIBLING = 0
    PREV_SIBLING = 1
    CHILD_CONTOUR = 2
    PARENT_CONTOUR = 3

    
    for f in fn:
        frame = cv.imread(f)
        # меняем цветовую модель с BGR на GRAY scale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        _, binary = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

        # ищем контуры и складируем их в переменную contours
        '''
        cv2.RETR_LIST       → Retrieve all contours
        cv2.RETR_EXTERNAL   → Retrieves external or outer contours only
        cv2.RETR_CCOMP       → Retrieves all in a 2-level hierarchy
        cv2.RETR_TREE       → Retrieves all in the full hierarchy
        '''
        
        if mode == 1:
            contour_type = cv.RETR_LIST
        elif mode == 2:
            contour_type = cv.RETR_EXTERNAL
        elif mode == 3:
            contour_type = cv.RETR_CCOMP
        elif mode == 4:
            contour_type = cv.RETR_TREE
        else:
            contour_type = cv.RETR_LIST

        contours, hierarchy = cv.findContours(binary,  contour_type, cv.CHAIN_APPROX_SIMPLE)

        # Iterate over top-level contours
        try:
            for count_i, value_i in enumerate(hierarchy[0]):
                
                if count_i >= 0:
                    count_i = hierarchy[0][count_i][NEXT_SIBLING]
            
                    # This must be a top-level contour
                    hierarchy[0][count_i][PARENT_CONTOUR] == -1

                    if hierarchy[0][count_i][CHILD_CONTOUR] == -1:
                        # This contour has no children, draw it red for demonstration purposes
                        cv.drawContours(frame, contours, count_i, (0, 0, 255), -1)

                    print("Contour with children: #", count_i, " r=", cv.boundingRect(contours[count_i]), " h=", hierarchy[0][count_i])

                    # This contour has children, draw it blue for demonstration purposes
                    cv.drawContours(frame, contours, count_i, (255, 0, 0), -1)

                    # Iterate over all direct children
                    for count_j, value_j in enumerate(hierarchy[0]):
                        if count_j >= 0:
                            #hierarchy[0][count_i][CHILD_CONTOUR]
                            count_j = hierarchy[0][count_j][NEXT_SIBLING]
                            print(" * Child contour: #", count_j, " r=", cv.boundingRect(contours[count_j]), " h=", hierarchy[0][count_j])

                            cv.drawContours(frame, contours, count_j, (0, 255, 0), -1)
                
                pass
        except TypeError:
            pass

        #print(hierarchy)
        #print(contours)

        # отображаем контуры поверх изображения
        #cv.drawContours(frame, contours, -1, (255, 0, 0), 3, cv.LINE_AA, hierarchy, 1)
        
        fname = str(os.path.splitext(f)[0]) + '_contour' + str(os.path.splitext(f)[-1])
        
        cv.imwrite(fname, frame)
        fn_result_list.append(fname)

        # выводим итоговое изображение в окно
        #cv.imshow('contours', frame)

        #cv.waitKey()
        #cv.destroyAllWindows()
        
    return fn_result_list
