#ahmad luthfi hanif, tutorial 14

import cv2

img=cv2.imread('depresiface.jpg')
#cv2.imshow('Gambar 1',img)
#cv2.waitKey(0)
imgrezised=cv2(img,(600,800))

#cv2.imshow('Gambar 1',img)
#cv2.waitKey(0)

#imggray= cv2/cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgblur= cv2.GaussianBlur(img,(5,5),1)
#cv2.imshow('gray',imggray)
#cv2.imshow('blur',imgblur)
#cv2.waitKey(0)

imgcanny=cv2.Canny(img,150,200)
kernel=np.ones((5,5),np.unit8)
imgDilation=cv2.dilate(imgcanny,kernel,iterations=1)
imgEroded=cv2.erode(imgcanny,kernel,iterations=1)
imgEroded2=cv2.erode(img,kernel,iterations=1)

imgcropped=img[0:100,0:200]
cv2.imshow('imgcanny',imgcanny)
cv2.imshow('imgdil',imgDilation)

cv2.waitKey(0)