from detector import Detector
import numpy as np
from tracker import initialization_tracks
if __name__ == "__main__":
    detections = np.array([[1,2,3,4],[2,3,4,5],[2,3,4,5]])
    trackings = initialization_tracks(measurements=detections , start=4 , verbose=True)
    stream_dict={}
    stream_dict["length"] = 2
    print(*deletion_condition(trackings , stream_dict))
