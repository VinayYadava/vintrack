import torch
import numpy as np

if __name__ == '__main__':


    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    
    
    
    # Images
    imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images
    
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
    
    