# _*_ coding=utf-8 _8_
#Wu Miao
import cv2
import matplotlib.pyplot as plt
#create a VideoCapture object
cap = cv2.VideoCapture(2)
'''
cap.set(3, 825)#set width
cap.set(4, 620)#set height
'''
k = 0
i=1
red = (0,0,255)

while k != 27:
    #ret: successfully read
    ret, frame = cap.read()

    if frame is None:
        break
    else:
        #visualize
        cv2.line(frame,(0,430),(640,430),red)
        cv2.imshow("video", frame)
        k = cv2.waitKey(20) & 0xff
        #ESC to exit

    "press q to save current frame"
    if k==ord('q'):
        cv2.imwrite('camera_cal/calibration%d.jpg' %i,frame)
        i=i+1


cap.release()
