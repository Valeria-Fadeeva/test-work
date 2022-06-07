#!/usr/bin/env python3

import os
import app


if __name__ == '__main__':
    
    '''
    cv2.RETR_LIST       → Retrieve all contours
    cv2.RETR_EXTERNAL   → Retrieves external or outer contours only
    cv2.RETR_CCOMP       → Retrieves all in a 2-level hierarchy
    cv2.RETR_TREE       → Retrieves all in the full hierarchy
    '''
        
    #filename = './images/cv_sample.png'
    filename = './images/i006.png'
    #filename = './images/i021.png'
    app.main(filename, mode=2)
