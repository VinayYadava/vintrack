import numpy as np
import cv2
from crop_detections_from_image import crop_detection_from_image
import torch

if __name__ == '__main__':
    img=cv2.imread("zidane.jpg")
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    x1,y1,x2,y2 = *(743,   48) ,*(1141,  720)
    x,y,w,h = x1,y1,x2-x1 ,y2-y1
    det = [x,y,w,h]

    imgs = [img.copy()]
    # Inference
    results1 = model(imgs)
    
    # Results
    results1.print()
    results1.save()  # or .show()
    predictions1 = results1.pred[0].numpy()
    predictions1[: ,4] = predictions1[:,4] * 100
    predictions1[:,2:4] = predictions1[:,2:4] - predictions1[:,0:2]
    predictions1 = predictions1.astype(np.int32)


    img1 = crop_detection_from_image(img = img.copy() , det = det)
    imgs = [img1.copy()]
    # Inference
    results2 = model(imgs)
    
    # Results
    results2.print()
    results2.save()  # or .show()
    predictions2 = results2.pred[0].numpy()
    predictions2[: ,4] = predictions2[:,4] * 100
    predictions2[:,2:4] = predictions2[:,2:4] - predictions2[:,0:2]
    predictions2 = predictions2.astype(np.int32)

    print(predictions1)
    print(predictions2)


    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()
