from apputils import get_adjusted_predictions_accd_crop,draw_bbox_rect , draw_predicted_bboxes, crop_img
import cv2
from detector import Detector
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("OIP.jpg")
    model = Detector("yolov5n").model
    h,w,_ = img.shape
    cropped_img = crop_img(img, (50,50,w,h))
    cv2.imshow("crop",cropped_img)
    print(img)
    h,w,_ = img.shape
    predictions = model(cropped_img).pred[0].numpy()
    predictions[: ,4] = predictions[:,4] * 100
    predictions[:,2:4] = predictions[:,2:4] - predictions[:,0:2]
    predictions = predictions.astype(np.int32)
    image = draw_predicted_bboxes(cropped_img,predictions,thickness =1,
    color=(255, 0, 0),
    text = "",
    font_size = 12)
    cv2.imshow("image",image)

    cv2.imshow("wing",img)
    if cv2.waitKey() & 0xFF==ord('q'):
        cv2.destroyAllWindows()

