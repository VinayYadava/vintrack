import numpy as np
import cv2

arr = np.load("imgs.npy")
print(arr.shape)
def find_most_occured_at_i_and_j(imgs,i,j):
    ar, counts = np.unique(ar = imgs[:,j,i] , return_counts=True , axis = 0 )
    return ar[np.argmax(counts)]

def find_mode_image(imgs):
    _,h,w,c = imgs.shape
    temp = np.zeros((h,w,c))
    for i in range(w):
        for j in range(h):
            temp[j,i,:]=find_most_occured_at_i_and_j(imgs,i,j)
        
            
    return temp.astype(np.int8)


#(195, 183, 176)
image = find_mode_image(arr)
print(image.shape)

np.save("image.npy",image,allow_pickle=True)

cv2.imshow("img", image)

if cv2.waitKey() & 0xFF==ord('q'):
    cv2.destroyAllWindows()
