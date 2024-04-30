import numpy as np
import cv2
from apputils import draw_rect


if __name__ == '__main__':
    text = "vinay"
    
    img = np.zeros((800,800,3))
    rect = (0,-10,100,100)
    x1,y1,w,h = rect

    img = draw_rect(rect= rect , img = img , thickness = -1 , color = (255,0,0),text = "vinay",font_size= 12)
    cv2.imshow("image", img)

    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()