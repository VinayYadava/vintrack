import cv2
import numpy as np
from apputils import draw_predicted_bboxes

if __name__ == '__main__':
    img = np.zeros((800 , 800,3))

    bboxes = [(20,20,100,100 ,0,1),(150,150,100,100,9,2),(500,500,100,100,0,3)]
    img = draw_predicted_bboxes(img=img,predictions=bboxes,thickness=2,color=(250,0,0),font_size=12)
    cv2.imshow("image", img)

    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()