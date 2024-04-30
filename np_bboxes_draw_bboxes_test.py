import cv2
import numpy as np
from apputils import draw_predicted_bboxes

if __name__ == '__main__':
    predictions = np.array([[     118.46,      175.32,      151.96,      196.06,     0.73034,           2],
 [     233.18,       159.6,       255.7,       177.1,     0.67195,           2],
 [     385.03,      150.96,      403.87,      166.52,     0.57358,           2],
 [     261.97,      140.46,       278.7,      152.41,     0.48821,           2],
 [     385.94,      150.66,      403.44,      166.15,     0.33735,           7]],dtype=np.int64)
    print(predictions)

    img = np.zeros((800,800,3))
    img = draw_predicted_bboxes(img = img,predictions=list(predictions),thickness=2 , color=(255,0,0),font_size=12)
    cv2.imshow("image", img)

    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()