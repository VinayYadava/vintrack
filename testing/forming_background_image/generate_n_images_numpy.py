import cv2
import numpy as np
video = "highway.mp4"
cap = cv2.VideoCapture(video)

imgs = []
for i in range(20):
    ret , frame = cap.read()
    imgs.append(frame)

imgs = np.array(imgs)
np.save("imgs.npy",imgs,allow_pickle=True)