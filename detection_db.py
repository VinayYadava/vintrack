import sqlite3

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
        self.time = time
        self.uid = uid
        self.features = features
        self.x, self.y, self.w, self.h = bbox
        self.db = db
        self.label = label
        self.video_id = video_id

    def insert_entry(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cmd = "INSERT INTO detections (time, uid, video_id, x, y, w, h, features, label) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(cmd, (self.time, self.uid, self.video_id, self.x, self.y, self.w, self.h, self.features, self.label))
        conn.commit()
        conn.close()
        print("Entry inserted successfully.")

if __name__ == "__main__":

    # Example usage:
    # Create the database file and table
    create_database("detections.db")
    
    # Create an Entry object and insert it into the database
    entry = Entry("2024-04-24 12:00:00", (10, 10, 100, 100), "Some features", "user123", "detections.db", "car", "video123")
    entry.insert_entry()
