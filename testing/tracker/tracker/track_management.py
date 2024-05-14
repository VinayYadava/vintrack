import numpy as np
from detection_db import create_database , Entries

def initialization_tracks(measurements , start , verbose = False):
    measurements_copy = measurements.copy()
    l , _  = measurements_copy.shape
    stop = start+l

    arr = np.arange(start , stop )

    initialized_tracks = list(zip(measurements_copy , arr))

    if verbose:
        print("-----------------------------------------------------------------\
              ----------------------------")
        print("Tracking ids get initialized for input measurements:")
        print(*initialized_tracks)
        print("-----------------------------------------------------------------\
              ----------------------------")

    return initialized_tracks

def deletion_condition(tracks , stream_info):
    length = stream_info['length']
    array_elements = np.array([x[0] for x in tracks])
    for i , item in enumerate(array_elements):
        print(item[1])
        if item[1]<=length:
            tracks.pop(i)
    return tracks

def save_tracks(dbname , tracks, video_id):
    try:
        create_database(dbname)
        # Create an Entry object and insert it into the database.
        entry = Entries(db= "detections.db", video_id = video_id,\
                        predictions = tracks , tracking = True)
        entry.insert()
        return True
    except Exception as e:
        print(e)
        return False
