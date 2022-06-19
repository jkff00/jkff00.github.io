import cv2 as cv
import os
img_file = 'C:/Users/admin/Desktop/(27).jpg'
winName = 'Color of thee rainbow'
img_bgr = cv.imread(img_file,1)
img_hsv = cv.cvtColor(img_bgr,cv.COLOR_BGR2HSV)
cv.namedWindow(winName)#滑动窗口命名
def nothing(x):
    print(x)
    pass

cv.createTrackbar('lowerH',winName,0,255,nothing)
cv.createTrackbar('lowerS',winName,0,255,nothing)
cv.createTrackbar('lowerV',winName,0,255,nothing)
cv.createTrackbar('highH',winName,0,255,nothing)
cv.createTrackbar('highS',winName,0,255,nothing)
cv.createTrackbar('highV',winName,0,255,nothing)

while(1):
    lowerH = cv.getTrackbarPos('lowerH',winName)
    lowerS = cv.getTrackbarPos('lowerS', winName)
    lowerV = cv.getTrackbarPos('lowerV', winName)
    highH = cv.getTrackbarPos('highH', winName)
    highS = cv.getTrackbarPos('highS', winName)
    highV = cv.getTrackbarPos('highV', winName)
    fire=cv.inRange(img_hsv, (lowerH,lowerS,lowerV),(highH,highS,highV))#根据滑块信息 得到二值化图像

    img_specifiedColor=cv.bitwise_and(img_hsv,img_hsv,mask=fire)

    cv.imshow(winName,img_specifiedColor)
    cv.imshow('fire',img_bgr)
    if cv.waitKey(1)==ord('q'):
        break
cv.detroyAllWindows()