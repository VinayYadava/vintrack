import cv2
import numpy as np

imgs = np.load('imgs.npy')
cap = cv2.VideoCapture("highway.mp4")
while cap:
    ret , frame = cap.read()
    if not ret:
        cv2.destroyAllWindows()
        break
    cv2.imshow("Window1" ,frame )
    cv2.imshow("Window2" ,frame / 255 )
    cv2.imshow("Window2" ,frame * 2 )
    if cv2.waitKey(25) & 0xFF==ord("q"):
        cv2.destroyAllWindows()
        break
    
def gaussian_img(img):
    np.dist