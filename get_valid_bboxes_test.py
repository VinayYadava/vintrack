import cv2
import numpy as np
from apputils import draw_predicted_bboxes,get_valid_bboxes,get_edges_from_points,draw_polygon

if __name__ == '__main__':
    img = np.zeros((800 , 800,3))
    roi = [(0,0),(200,0),(200,200),(0,200)]
    
    edges = get_edges_from_points(points=roi , verbose=False)
    bboxes = [(20,20,100,100),(150,150,100,100),(500,500,100,100)]
    print("bboxes :" ,bboxes)
    valid_bboxes = get_valid_bboxes(bboxes=bboxes , edges = edges)
    print("valid_bboxes :",valid_bboxes)

    img = draw_polygon(frame = img, points=roi)

    img1 = draw_predicted_bboxes(img=img.copy(),predictions=bboxes,thickness=2,color=(250,0,0),text="vinay",font_size=12)
    img2 = draw_predicted_bboxes(img=img.copy(),predictions=valid_bboxes,thickness=2,color=(250,0,0),text="vinay",font_size=12)

    cv2.imshow("Image with all Bounding Boxes", img1)
    cv2.imshow("Image with Valid Bounding Boxes", img2)

#
    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()