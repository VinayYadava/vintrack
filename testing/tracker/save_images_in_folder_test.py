from detector.detection_db import Entries, create_database, save_images_in_folder
from cv2 import imread
from datetime import datetime
img = imread("download.jpg")
time = datetime.now(tz = "")
save_images_in_folder(imgs=[img] , timestamp=4, folder = "detections",tracking_ids=[8])

