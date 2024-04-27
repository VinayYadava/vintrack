from detector import Detector
import cv2
det = Detector("yolov5s")

mod = det.model

img = "download.jpg"
img = cv2.imread(img)
cv2.imshow("image",img)
mod(img)
if cv2.waitKey() & 0xFF == ord("q"):
    cv2.destroyAllWindows()