#coding:utf-8
#Wu Miao
import cv2
import numpy as np
from balltrack import get_ball_position2

cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

k = 0
i = 0
position_x = np.zeros(1000)
position_y = np.zeros(1000)
position_x_image = np.zeros(1000)
position_z = np.zeros(1000)

while k != 27:

    ret1,img1 = cap1.read(1)
    #ret2,img2 = cap2.read(2)
    #print('begin to process image...')
    
    processed_img1,x,y = get_ball_position2(img1)#top view
    #processed_img2,x_image,z = get_ball_position1(img2)#side view
    
    "show the image after processed"
    cv2.imshow("detected top view",processed_img1)
    cv2.imwrite('E:/camera12/topview_test3_%04d.jpg' % i, processed_img1)
    #cv2.imshow("detected side view",processed_img2)
    #cv2.imwrite('E:/camera11/sideview_test3_%04d.jpg' % i, processed_img2)
    
    print('the coordinate of ball in image frame is:',x,y)
    "x,y in pixel coordinate"

    #position_x[i]=x
    #position_y[i]=y
    #position_x_image[i]=x_image
    #position_z[i]=z

    if i == 1000:
        break

    i = i+1

    # keyboard input0
    k = cv2.waitKey(20) & 0xff

#np.savetxt("E:/camera11/test3_data.csv",(position_x,position_y,position_x_image,position_z),delimiter=",")







