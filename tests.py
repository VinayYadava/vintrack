from detector import Detector

       
#if __name__ == "__main__":
#    det = Detector("yolov5s")
#    model = det.model
#    result = model("download.jpg")
#    result.show()
#
#
import cv2
from utils import show_video, select_roi
from detector import Detector

    
if __name__=="__main__":
    #video_path = "demo.mp4"
    video_path = "highway.mp4"
    det = Detector("yolov5s")
    model = det.model
    #show_video(video_path=video_path , detect_flag=True)