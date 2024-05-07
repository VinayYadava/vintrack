import cv2
import numpy as np

def crop_detection_from_image(img,det):
    img[det[1]:det[1]+det[3],det[0]:det[0]+det[2],:]= np.zeros((det[3],det[2],3))
    return img

if __name__ == '__main__':
    img=cv2.imread("zidane.jpg")
    x1,y1,x2,y2 = *(743,   48) ,*(1141,  720)
    x,y,w,h = x1,y1,x2-x1 ,y2-y1
    det = [x,y,w,h]

    img = crop_detection_from_image(img=img, det = det)

    cv2.imshow("img",img)

    if cv2.waitKey() & 0xFF == ord('q'):
        cv2.destroyAllWindows()