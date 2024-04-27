import sqlite3
from datetime import datetime

def create_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the detections table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            time TEXT,
            uid TEXT,
            video_id TEXT,
            x REAL,
            y REAL,
            w REAL,
            h REAL,
            features TEXT,
            label TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Table 'detections' created successfully.")

class Entry:
    def __init__(self, time, bbox, features, uid, db, label, video_id):
        self.db = db
        self.entries = []

    def add_entry(self, time, bbox, features, uid, label, video_id):
        if len(self.entries)==50:
            self.insert_entries()
        x,y,w,h = bbox
        self.entries.append((time, uid, video_id, x, y, w, h, features, label))
        pass
    
    def insert_entries(self):
        if not self.entries:
            return  # No entries to insert
        
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cmd = "INSERT INTO detections (time, uid, video_id, x, y, w, h, features, label) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(cmd, self.entries)
        conn.commit()
        conn.close()
        print("Entries inserted successfully.")



if __name__ == "__main__":

    # Example usage:
    # Create the database file and table
    create_database("detections.db")
    
    # Create an Entry object and insert it into the database
    entry = Entry(datetime.now(), (10, 10, 100, 100), "Some features", "user123", "detections.db", "car", "video123")
    entry.insert_entry()
