import subprocess as sp 
import os
import numpy as np
import cv2
 

saved_np_array = "imgs.npy"

if not os.path.exists(saved_np_array):
    cmd = "python generate_n_images_numpy.py"
    sp.run(args = cmd)
    print(f"generating '{saved_np_array}'")
else:
    print(f"using saved '{saved_np_array}'")

def max_min_image(imgs,alpha,beta):
    imin = np.min(imgs.copy(),axis= 0)
    imax = np.max(imgs.copy() , axis = 0)
    print("imin shape: ", imin.shape)
    print("imax shape: ", imax.shape)

    im = alpha * imin + beta * imax
    return im.copy()

def max_image(imgs):
    imax = np.max(imgs.copy() , axis = 0)
    return imax.copy()

def min_image(imgs):
    print(imgs[:,0,0,0])
    imin = np.min(imgs.copy() , axis = 0)
    return imin.copy()

def median_image(imgs):
    imedian = np.median(imgs.copy() , axis = 0)
    return imedian.copy()

def mode_image(imgs):
    imode = stats.mode(imgs.copy() , axis = 0)
    return imode.copy()

print("-----------------------------------------------------------------------------------------------------------------------------------")

imgs = np.load(saved_np_array).copy()
print(imgs.shape)



img1 = imgs[9].copy()
cv2.imshow("img" ,img1)


img2 = max_image(imgs.copy())
print(img2.shape)
cv2.imshow("img with max method" ,img2)

img3 = min_image(imgs.copy())
print(img3.shape)
cv2.imshow("img with min method" ,img3)
print(img3[0,0,0])

img4 = median_image(imgs.copy()).astype(np.int8)

print(img4.shape)
cv2.imshow("img with median method" ,img4)

#rect = cv2.selectROI("img" , img)
#print(rect)
x,y,b,h = (114, 173, 41, 24)

#img[y:y+h,x:x+b] = np.zeros((24,41,3))
#img5 = mode_image(imgs.copy())
#print(img5.shape)
#cv2.imshow("img with median method" ,img5)

alpha = 0.001
beta =  0.5

gamma = 1.5

img =  gamma*(alpha * img4 + beta * img2)
cv2.imshow("mixed" , img.astype(np.int8))


if cv2.waitKey() & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    exit()