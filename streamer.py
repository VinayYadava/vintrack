import cv2
from apputils import show_video, select_roi

    
if __name__=="__main__":
    #video_path = "demo.mp4"
    video_path = "highway.mp4"
    
    #If not want to save detections in db.
    show_video(video_path=video_path , detector_name="yolov5s",save_in_db=True)
    #If not want to save detections in db.
    #show_video(video_path=video_path , detector_name="yolov5s",save_in_db=True)