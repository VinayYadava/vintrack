import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("zidane.jpg")
points = [(743,   48) ,(1141,  720) ]

plt.scatter(x = [743,1141] , y =[28,720])


plt.show()
img = cv2.rectangle(img,pt1= points[0], pt2 = points[1] ,color = (255,0,0),thickness =-1)
cv2.imshow("img",img)
cv2.imwrite("myimg.jpg",img)

if cv2.waitKey() & 0xFF==ord("q"):
    cv2.destroyAllWindows()
    exit()