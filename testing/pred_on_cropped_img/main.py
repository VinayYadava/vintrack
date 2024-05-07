import torch
import numpy as np
import cv2

if __name__ == '__main__':


    
    
    
    
    
    # Images
    img = cv2.imread('zidane.jpg')
    x1,y1,x2,y2 = *(743,   48) ,*(1141,  720)
    t = img[x1:x2,y1:y2,:]
    print(t)
    cv2.imshow("ff",t)
    cv2.waitKey()
    imgs = [img]  # batch of images
    
    # Inference
    results = model(imgs)
    
    # Results
    results.print()
    results.save()  # or .show()
    predictions = results.pred[0].numpy()
    predictions[: ,4] = predictions[:,4] * 100
    predictions[:,2:4] = predictions[:,2:4] - predictions[:,0:2]
    predictions = predictions.astype(np.int32)
    print(predictions)
    
    