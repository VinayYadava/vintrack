import cv2
from apputils import show_video , is_inside,get_edges_from_points


if __name__ == '__main__':
    # If want to display video without Detections
    roi =  [(10, 10), (10, 200), (200, 200), (200, 10)]
    #show_video(video_path="highway.mp4",param = roi)

    edges = get_edges_from_points(roi)

    xp , yp = (5,20)

    v = is_inside(edges = edges , xp  = xp , yp = yp)
    if v ==0:
        print("Not in ROI")
    else:
        print("Yes inside ROI")
    print(v)

    