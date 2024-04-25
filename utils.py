import cv2
import numpy as np

def show_video(video_path , detect_flag):
    
        
    flagInitial = True
    win = f"Streaming {video_path}"
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened() :
        print("Error: Could not open video file.")
        exit()
    roi = []
    roi_drawn_flag=False
    while cap:
        ret , frame = cap.read()

        if not ret:
            break
        if len(roi)!=0:
            if not roi_drawn_flag:
                frame = draw_polygon(frame,roi)
                

        cv2.imshow(
            winname = win ,mat=frame
            ) 
        
        #cv2.namedWindow("Frame")
        #cv2.createButton(win,echo,None,cv2.QT_PUSH_BUTTON,1)
        #cv2.createButton(
        #    buttonName = "Select ROI",
        #    onChange=roi_button_callback,
        #    initialButtonState=0
        #    )
        if flagInitial:
            roi_flag=False
            print("-------------------------------------------------------------------------------------")
            print("------------------------------------- Input ROI Points ------------------------------")
            print("-------------------------------------------------------------------------------------")

            while roi_flag !=True:
                roi , roi_flag = get_roi_points(frame, roi)
                if roi_flag:
                    flagInitial =False
            
        #if detect_flag:
        #    mod(frame).show()


        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

def select_roi(img, verbose):
    rect = cv2.selectROI(
        windowName="selecting region of intrest",
        img = img,
    )
    cv2.destroyWindow("selecting region of intrest")
    if verbose:
        print(rect)
    return rect
pts = []
def mouse(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pts.append((x,y))
        print((x,y))


def draw_rect(rect,img):
    x1,y1,w,h = rect
    
    img_with_rect = cv2.rectangle(
        img = img,
        pt1=(x1,y1),
        pt2=(x1+w,y1+h),
        thickness=2,
        color=(255,255,255)
                  )
    
    return img_with_rect

def draw_bbox_in_roi(rect , img):
    pass

def draw_polygon(frame,points):
    points = np.array(points)
    r,c=points.shape 
    points = points.reshape((-1,r,c))
    frame = cv2.polylines(img=frame , pts=points, isClosed = True,color = (255,255,255),thickness=5,)
    return frame

def draw_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        print(f"Left button clicked at ({x}, {y})")
        param[1].append((x,y))
        param[0]=cv2.circle( param[0],(x, y), 5, (255, 255, 255), -1)
        return param[1]

def get_roi_points(frame,points):
    flag=False
    
    param = [frame , points]
    cv2.imshow("Select ROI points", frame)
    cv2.setMouseCallback("Select ROI points", draw_point, param=param)
             
    if cv2.waitKey() & 0xFF==ord("s"):
        if len(points)>=3:
            print("-------------------------------------------------------------------------------------")
            print("-----------------------------------Final Points In ROI-------------------------------")

            cv2.destroyWindow(winname="Select ROI points")
            flag=True
            print(f"Selected Points in roi is {points}.")
            print("-------------------------------------------------------------------------------------")

        else:
            print("Kindly select atleast 3 points.")
            flag=False
    return points, flag

def click_event(event,x,y):
    if event == cv2.EVENT_LBUTTONDOWN :
        print(f"Left button clicked at ({x}, {y})")
    
def echo():
    print("vinay")
def is_inside(edges, xp , yp):
    cnt = 0
    for edge in edges:
        (x1,y1),(x2,y2) = *edge[0],*edge[1]
        if (yp<y1) != (yp<y2) and xp < (x2-x1)*((yp-y1)/(y2-y1)+x1):
            cnt+=1
    
    return cnt

def orientation(p1 , p2 ,p3):
    x1 , y1 , x2, y2 , x3 , y3 = *p1 , *p2 , *p3
    d= (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
    if d>0 :
        return 1
    elif d<0:
        return -1
    else:
        return 0
    
def gift_wrapping(points):
    on_hull = min(points)
    hull = []
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o= orientation(on_hull, next_point , point)
            if next_point == on_hull or o==1 or (0 ==0 and dist(on_hull,point) > dist(on_hull,next_point)):
                next_point = point
        on_hull = next_point
        if on_hull == hull[0]:
            break

def dist(p1,p2):
    x1,y1 ,x2,y2 = *p1 , *p2
    return 
#def make_edges_for_closed_polygon(points):

# Example usage:
polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
point = (2, 2)
##print(is_inside(*point, polygon))
