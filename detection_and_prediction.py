#coding utf-8
#2019-5-25，Wu Miao

import cv2
import numpy as np
from balltrack import get_ball_position1
from spot_prediction import side_view_prediction

cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

k = 0
i = 0
m = 0
pre_z = 240
position_x_image = np.zeros(3)
position_z = np.zeros(3)
data_x = np.zeros(1000)
data_z = np.zeros(1000)
data_pre_z =np.zeros(1000)

while k != 27:

    ret1, img1 = cap1.read(1)
    ret2, img2 = cap2.read(2)
    # print('begin to process image...')

    processed_img1, x, y = get_ball_position1(img1)  # top view
    processed_img2, x_image, z = get_ball_position1(img2)  # side view

    "x,y in pixel coordinate"
    print('the coordinate of ball in image frame is:', x, y, x_image, z)

    "save the valid data for spot predition"
    if i<=3:
        if x_image != -320 or z != 240:
            position_x_image[i] = x_image
            position_z[i] = z
            i=i+1

    "if there are 3 set of position data, call prediction function"
    if i==4 :
        pre_z = side_view_prediction(position_x_image,position_z,-320)
        print("Predicted z：",pre_z)

        if pre_z != 240.0:
            i = 5
        else:
            i = 0

    "show the image after processed"
    cv2.circle(processed_img2, (0, 240-int(pre_z)), 2, (0, 0, 0), 10)
    cv2.imshow("detected top view", processed_img1)
    cv2.imwrite('E:/camera9/topeview_test_%04d.jpg' % m, processed_img1)
    cv2.imshow("detected side view", processed_img2)
    cv2.imwrite('E:/camera9/sideview_test_%04d.jpg' % m, processed_img2)

    "to save data"
    if m==1000:
        print("Overflow of data")
        break
    else:
        data_x[m] = x_image
        data_z[m] = z
        data_pre_z[m] = pre_z
        m=m+1


    # keyboard input0
    k = cv2.waitKey(20) & 0xff

np.savetxt("E:/camera9/test3_data.csv",(data_x,data_z,data_pre_z),delimiter=",")

