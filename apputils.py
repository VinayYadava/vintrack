import matplotlib.pyplot as plt
from detection_db import create_database , Entries
import cv2
import numpy as np
from detector import Detector

def show_video(video_path , detector_name=None ,save_in_db = False , db_name = None , param=False):
    
        
    flagInitial = True
    win = f"Streaming {video_path}"
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened() :
        print("Error: Could not open video file.")
        exit()
    if detector_name:
        print("Creating Detector...")
        detection_model = Detector(detector_name).model
    if save_in_db:

        if not db_name:
            db_name = "detections.db"
        create_database(db_name)  
    if param:
        roi = param
    else:
        roi = []
        edges = []
    roi_drawn_flag=False
    
    while cap:
        ret , frame = cap.read()

        if not ret:
            break
        if len(roi)!=0:
            if not roi_drawn_flag:
                frame = draw_polygon(frame,roi)

                
        if detector_name:
            detections = detection_model(frame)
            
            
        
        if not detector_name:
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
                    edges = get_edges_from_points(points=roi , verbose=False)
                    flagInitial =False
            
        if detector_name:
            
            predictions = detections.pred[0].numpy()
            
            predictions[: ,4] = predictions[:,4] * 100
            predictions[:,2:4] = predictions[:,2:4] - predictions[:,0:2]
            predictions = predictions.astype(np.int32)
            valid_bboxes = get_valid_bboxes(bboxes=list(predictions) , edges = edges)
            
            if len(valid_bboxes)==0:
                cv2.imshow("streaming...", frame)
                
            else:
                im = draw_predicted_bboxes(img=frame.copy(),predictions=valid_bboxes,thickness=2,color=(250,0,0),text="vinay",font_size=12)

                cv2.imshow("streaming...", im)
            if save_in_db:
                valid_bboxes = np.array(valid_bboxes)
                if valid_bboxes.shape[0] !=0:
                    entry = Entries(db= "detections.db", video_id= "video123",pred = valid_bboxes)
                    entry.insert(verbose=True)
                else:
                    print("Nothing to insert")
            
            

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

def add_label_on_bbox(image ,rect , color,text,font,font_size,font_thickness,padding = 4):
    font_scale = cv2.getFontScaleFromHeight(fontFace=font, pixelHeight= font_size,thickness=font_thickness)
    x1,y1,w,h = rect
    
    if y1-font_size-padding>=0  :
        x1 = x1
        ydash = y1-font_size-padding
        w1 = font_size*len(text) + 2*padding
        h1 = y1-ydash
        rect1  = [x1,ydash,w1,h1]
        orgx= x1+padding
        orgy= y1-padding
        org = (orgx ,orgy)
    else:
        x1 = x1
        ydash = y1+h
        w1 = font_size*len(text) + 2*padding
        h1 = 2*padding + font_size 
        rect1  = [x1,ydash,w1,h1]
        orgx= x1+padding
        orgy= y1+h+font_size
        org = (orgx ,orgy)

    image = draw_rect(rect1 ,image  ,-1 , color , None) 
    image = cv2.putText(img = image,text=text , org = org,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=font_scale,color=(255,255,255),thickness=1)

    return image

def draw_rect(rect,img,thickness , color , text= None , font_size = None):
    x1,y1,w,h = rect
    

    img_with_rect = cv2.rectangle(
        img = img,
        pt1=(x1,y1),
        pt2=(x1+w,y1+h),
        thickness=thickness,
        color=color
                  )
    if text:
        if font_size :
            img_with_rect = add_label_on_bbox(img_with_rect,rect,(0,255,0),text,cv2.FONT_HERSHEY_COMPLEX_SMALL,12 , 2 , 4)

            
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
        param[0]=cv2.circle( param[0],(x, y), 5, (255, 255, 255), 2)
        return param[1]
def get_edges_from_points(points , verbose= False):

    edges = []
    n = len(points)
    for i in range(n):
        if i == n-1 :
            l = points[i]
            r = points[0]
            edges.append([l,r])
            if verbose:
                print(f"The edges formed by given points are {edges}")

            return edges
        
        l = points[i]
        r = points[i+1]

        edges.append([l,r])
    
    return edges

def draw_predicted_bboxes(img , predictions,thickness = -1 , color = (255,0,0),text ="",font_size= 12):
    for i in predictions:
        bbox = i[:4]
        text = f"{i[5]}"
        img = draw_rect(bbox,img,thickness  , color ,text ,font_size)
    return img

def get_valid_bboxes(bboxes , edges):
    valid_bboxes = []
    for i in bboxes:
        
        if is_inside(edges = edges , xp = i[0],yp = i[1])==1:
            valid_bboxes.append(i)
    return valid_bboxes
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
        x1,y1,x2,y2 = *edge[0],*edge[1]
        if (yp<y1) != (yp<y2) and xp < (x1 + ((yp- y1)/(y2-y1))*(x2-x1)):
            cnt+=1
    
    return cnt%2

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


if __name__=="__main__":
    #video_path = "demo.mp4"
    video_path = "highway.mp4"
    #If not want to save detections in db.
    show_video(video_path=video_path , detector_name="yolov5s",save_in_db=False)
    #If not want to save detections in db.
    #show_video(video_path=video_path , detector_name="yolov5s",save_in_db=True)