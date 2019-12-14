#coding:utf-8
#2109-5-3,Wu Miao
import cv2
import matplotlib.pyplot as plt
import numpy as np

"""the program is used to extract position of ball in an image,
two methods are provided: 
1. for image with clear backgroud, calculate the midpoint od edges.
2. for image with more colorful background, use hough transformation.
The target ball is white"""

def get_ball_position1(img):
    """method 1: calculate the center point of detected cycle edge"""

    #detect the edges of ball from image
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    mask_white = cv2.inRange(gray_img,200,255)
    mask_img = cv2.bitwise_and(mask_white,gray_img)
    kernel_size = 3
    gaussblur_img = cv2.GaussianBlur(mask_img,(kernel_size,kernel_size),0)
    low_threshold = 200
    high_threshold = 255
    edge_img = cv2.Canny(gaussblur_img,low_threshold,high_threshold)
    #cv2.imshow("edge",edge_img)
    #cv2.waitKey(0)
    #cv2.imwrite('E:/image_output/gray.jpg',gray_img)
    #cv2.imwrite('E:/image_output/mask.jpg', mask_img)
    #cv2.imwrite('E:/image_output/edge.jpg', edge_img)

    if np.argmax(edge_img) == 0:
        center_x = 0
        center_y = 0
        #no edge is detected
    else:
        nonzero_row, nonzero_col = edge_img.nonzero()
        rowmax = np.argmax(nonzero_row)
        rowmin = np.argmin(nonzero_row)
        center_x = (nonzero_col[rowmax]+nonzero_col[rowmin])/2
        colmax = np.argmax(nonzero_col)
        colmin = np.argmin(nonzero_col)
        center_y = (nonzero_row[colmax]+nonzero_row[colmin])/2

    col_num = 640
    row_num = 480

    coor_x = center_x - col_num/2
    coor_y = row_num/2 - center_y

    cv2.circle(edge_img, (int(center_x), int(center_y)), 2, (0, 0, 255), 10)
    #cv2.imwrite('E:/image_output/track_method1_test4.jpg', edge_img)

    return img,coor_x,coor_y#origin locates in the center of picture


def get_ball_position2(img):
    """method 2: hough transformation to detect the center of cycle"""

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles1 = cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,600,param1=100,param2=30,minRadius=20,maxRadius=130)

    if circles1 is None:
        x = 0
        y = 0
    else:
        circles = circles1[0, :, :]
        circles = np.uint16(np.around(circles))
        #print('the number of circles:',circles.shape)
        for n in circles[:]:
            cv2.circle(img,(n[0],n[1]),n[2],(255,0,255),5)
            cv2.circle(img,(n[0],n[1]),2,(255,0,255),10)
            x=n[0]
            y=n[1]
            #x = (n[0]/col_num)*width
            #y = (n[1]/row_num)*height

    cv2.imwrite('E:/image_output/track_method2_test4.jpg', img)
    return img,x,y


if __name__ == '__main__':
    # read the image
    img = cv2.imread("E:/camera/sideview_test3_0063.jpg")
    #img = cv2.resize(img,(640,480),interpolation=cv2.INTER_CUBIC)

    # calculate the position of ball center
    row_num,col_num = img.shape[0],img.shape[1]
    #width = 2
    #height = 2

    ouput1,output2,output3=get_ball_position1(img)
    print(output2,output3)
