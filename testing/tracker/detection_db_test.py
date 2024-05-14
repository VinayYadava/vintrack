from detector.detector import Detector
from detection_db import create_database, Entries
from cv2 import imread
if __name__ == "__main__":

    # Example usage:
    # Create the database file and table
    det = Detector(name = "yolov5n")
    create_database("detections.db")
    IMAGE_PATH = "download.jpg"

    img = imread(IMAGE_PATH)
    print(img)

    mod = det.model
    if mod is None:
        print("mod is none !")
    prediction = mod(img).pred[0].numpy()

    print(prediction)

    # Create an Entry object and insert it into the database
    entry = Entries(db= "detections.db", video_id= "video123",predictions = prediction)
    entry.insert()
