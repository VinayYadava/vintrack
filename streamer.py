import cv2
from apputils import show_video, select_roi

    
if __name__=="__main__":
    #video_path = "demo.mp4"
    video_path = "highway.mp4"
    show_video(video_path=video_path , detector_name="yolov5s",save_in_db=True)