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
#循环
while k != 27:
    #ret表示读取是否成功，frame表示读取的帧的内容
    ret, frame = cap.read()

    if frame is None:
        break
    else:
        #调用openCV显示每一帧
        cv2.line(frame,(0,430),(640,430),red)#校正板子的位置
        cv2.imshow("video", frame)
        k = cv2.waitKey(20) & 0xff
        #27时ESC键，如果按下ESC键退出显示

    "键入q保存当前图片"
    if k==ord('q'):
        cv2.imwrite('camera_cal/calibration%d.jpg' %i,frame)
        i=i+1

#释放VideoCapture对象
cap.release()