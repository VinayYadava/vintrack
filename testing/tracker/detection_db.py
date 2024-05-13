import sqlite3
from datetime import datetime
import os
import logging

from cv2 import imread, imwrite
import numpy as np

from detector import Detector

def create_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the detections table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            time TEXT,
            video_id TEXT,
            x REAL,
            y REAL,
            w REAL,
            h REAL,
            confidence TEXT,
            label TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Table 'detections' created successfully.")

def save_image_in_folder(imgs, timestamp, folder, tracking_ids):
    try:
        for img in zip(imgs, tracking_ids):
            file = f"{timestamp}-{tracking_ids}.jpg"
            filepath = os.path.join(folder , file)
            imwrite(filename=filepath, img=img)
        return True
    except Exception as e:
        logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.exception("An error occurred: %s", e)

        print(f"failed to save img (check logs at {os.path.join(os.getcwd(), 'error.log')})")
        return False

class Entries:
    def __init__(self, db, video_id, predictions, tracking=None, save_crop=False):
        self.db = db
        self.predictions = predictions
        self.n , _ = self.predictions.shape
        if tracking:
            if save_crop:
                self.headers = np.tile(
                    A = np.array([str(datetime.now()), video_id]),\
                    reps = (self.n,1)
                    )     
            else:
                self.headers = np.tile(
                    A = np.array([str(datetime.now()), video_id]),\
                    reps = (self.n,1)
                    )
        else:
            self.headers = np.tile(
                A = np.array([str(datetime.now()), video_id]),\
                reps = (self.n,1)
                )
        self.entries = np.concatenate(
            (self.headers , self.predictions),
            axis = 1
        )

    def insert(self , verbose=True):
        l = len(self.entries)
        if l ==0:
            return  # No entries to insert

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cmd = "INSERT INTO detections (time, video_id, x, y, w, h, confidence, label)\
              VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(cmd, self.entries)
        conn.commit()
        conn.close()
        if verbose:
            print(f"{l} entries inserted successfully.")


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
