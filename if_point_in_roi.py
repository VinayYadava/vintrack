import cv2
from apputils import show_video , is_inside

if __name__ == '__main__':
    # If want to display video without Detections
    roi = []
    show_video(video_path="highway.mp4",param = roi)