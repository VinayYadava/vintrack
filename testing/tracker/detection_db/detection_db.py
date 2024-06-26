import sqlite3
from datetime import datetime
import os
import logging

import numpy as np

from cv2 import imwrite

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

def save_images_in_folder(imgs, timestamp, folder, tracking_ids):
    try:
        for img ,id in zip(imgs, tracking_ids):
            file = f"{timestamp}-{id}.jpg"
            if not os.path.exists(folder):
                os.mkdir(folder)
            filepath = os.path.join(folder , file)
            print(filepath)
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
