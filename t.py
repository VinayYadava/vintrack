
import cv2
cv2.namedWindow("Frame")
def echo():
    print("vinay")
cv2.createButton("vinay",echo,None,cv2.QT_PUSH_BUTTON,1)
        #cv2.createButton(
        #    buttonName = "Select ROI",
        #    onChange=roi_button_callback,
        #    initialB