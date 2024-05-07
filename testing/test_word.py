import cv2
from apputils import draw_text

path = "download.jpg"
img = cv2.imread(path)
text = "reptile"
text_img = draw_text(img,text=text,org=(0,10),font_size=0.5)

cv2.imshow("text_img",text_img)

if cv2.waitKey() & 0xFF == ord("q"):
    cv2.destroyAllWindows()
    exit()