#ahmad luthfi hanif, tutorial 13

import cv2

#img=cv2.imread('depresiface.jpg')
#cv2.imshow('Gambar 1',img)
#cv2.waitkey(0)

cap=cv2.VideoCapture(0)
cap.set(3,640) #dimensi lebar
cap.set(4,580) #dimensi tinggi
cap.set(10,1000) #brigthness

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitkey(1) &0xFF == ord('q')
        break