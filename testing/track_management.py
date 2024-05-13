
import numpy as np

def initialization_tracks(measurements , start , verbose = False):
    measurements_copy = measurements.copy()
    l , _  = measurements_copy.shape 
    stop = start+l
    
    arr = np.arange(start , stop )
    initialized_ids = np.expand_dims(arr , axis = 1)
    
    initialized_tracks = list(zip(measurements_copy , arr))
    
    if verbose:
        print("---------------------------------------------------------------------------------------------")
        print("Tracking ids get initialized for input measurements:")
        print(*initialized_tracks)
        print("---------------------------------------------------------------------------------------------")

    return initialized_tracks

def deletion_condition(tracks , stream_info):
    length = stream_info['length']
    array_elements = np.array([x[0] for x in tracks])
    for i , item in enumerate(array_elements):
        print(item[1])
        if item[1]<=length:
            tracks.pop(i)
    return tracks

def save_tracks():
    
    return
if __name__ == "__main__":
    measurements = np.array([[1,2,3,4],[2,3,4,5],[2,3,4,5]])
    tracks = initialization_tracks(measurements , 4 , verbose=True)
    stream_info={}
    stream_info["length"] = 2
    print(*deletion_condition(tracks , stream_info))