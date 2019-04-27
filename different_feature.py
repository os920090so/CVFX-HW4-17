import numpy as np
import cv2

#different feature extrators, e.g. SIFT, SURF
'''
#SIFT
imgname='car.jpg'
gray = cv2.imread(imgname,0)

sift = cv2.xfeatures2d.SIFT_create(2000)
kp, des = sift.detectAndCompute(gray,None)
# print('sift=',len(kp))
siftimg = cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('sift'+imgname,siftimg)

#SURF
surf = cv2.xfeatures2d.SURF_create(2500)
kp, des = surf.detectAndCompute(gray,None)
# print('surf=',len(kp))
surfimg = cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('surf'+imgname,surfimg)

#U-SURF(without orientation)
surf.setUpright(True)
kp, des = surf.detectAndCompute(gray,None)
# print('usurf=',len(kp))
surfimg = cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('u-surf'+imgname,surfimg)

# ORB=FAST + steer BRIEF -> only detect not compute
orb = cv2.ORB_create(2000)
kp, des = orb.detectAndCompute(gray,None)
# print('orb=',len(kp))
orbimg = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('orb'+imgname,orbimg)
'''
#TODO other feature extraction set the same number of keypoint compare image&time 

#measure
import timeit
testtime = 100

def mySIFT(gray):
    sift = cv2.xfeatures2d.SIFT_create(2000)
    kp, des = sift.detectAndCompute(gray,None)
    return kp,des

def mySURF(gray):
    surf = cv2.xfeatures2d.SURF_create(2500)
    kp, des = surf.detectAndCompute(gray,None)
    return kp, des

def myUSURF(gray):
    surf = cv2.xfeatures2d.SURF_create(2500)
    surf.setUpright(True)
    kp, des = surf.detectAndCompute(gray,None)
    return kp, des

def myORB(gray):
    orb = cv2.ORB_create(2000)
    kp, des = orb.detectAndCompute(gray,None)
    return kp, des

gray=cv2.imread('0.jpg',0)
t = timeit.timeit(stmt="mySIFT(gray)", setup="import numpy as np;import cv2;from  __main__ import mySIFT,gray;", number=testtime)/testtime
print('mySIFT=',t)

t = timeit.timeit(stmt="mySURF(gray)", setup="import numpy as np;import cv2;from  __main__ import mySURF,gray;", number=testtime)/testtime
print('mySURF=',t)

t = timeit.timeit(stmt="myUSURF(gray)", setup="import numpy as np;import cv2;from  __main__ import myUSURF,gray;", number=testtime)/testtime
print('myUSURF=',t)

t = timeit.timeit(stmt="myORB(gray)", setup="import numpy as np;import cv2;from  __main__ import myORB,gray;", number=testtime)/testtime
print('myORB=',t)