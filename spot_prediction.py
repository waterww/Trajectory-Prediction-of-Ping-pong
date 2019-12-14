#coding utf-8
#2019-5-20, Wu Miao
import numpy as np

def top_view_prediction(X,Y,x_t):
    p = np.polyfit(X,Y,1)#linear fit
    y_t = p[0]*x_t+p[1]#the predicted point

    return y_t

def side_view_prediction(X,Z,x_t):

    z_t=240

    T = np.arange(0, (1 / 30 * len(X)), 1 / 30)  # time

    "to delete undetected data"
    """n = (X!=-320)|(Z!=240)
    X = X[n]
    Z = Z[n]
    T = T[n]"""

    k=0.402#energy lose coefficient

    p1 = np.polyfit(T,X,1)
    V_x = p1[0]#calculate horizontal velocity

    t_t = (x_t-X[0])/V_x+T[0]#time needed to reach target position from time 0
    #print("Arrival time：",t_t)

    """for m in range(len(X)):#get position of first landing
        if m>=1:
            if Z[m]+50<Z[m-1] and Z[m]+50<Z[m+1]:

                Z1 = Z[:(m+1)]#keep position and time info of the first bounce period
                T1 = T[:(m+1)]
                break
    """
    p2 = np.polyfit(T,Z,2)#second order fit to calculate g,v,h
    g = -2*p2[0]

    V_z = np.zeros(50)#initial vertical velocity of every bounce period
    T_crash = np.zeros(50)#time needed for every bounve period

    for i in range(50):

        if i == 0:
            #T_crash[i] = T1[-1]
            p = np.poly1d(p2+[0,0,210])
            T_crash[i] = p.r[1]
            V_z[i] = -p2[1]+g*T[-1]
        else:
            V_z[i] = k*V_z[i-1]#initial vertical velocity of each run
            T_crash[i] = 2*V_z[i]/g#time consumed for each run

        "to decide whether the ball arrive target place in the bounce"
        if np.sum(T_crash)>= t_t:
            t_n = t_t-np.sum(T_crash[:i])
            z_t = V_z[i] * t_n - (1 / 2) * g * (t_n ** 2)-210
            break

    #print("X coordinate：",X)
    #print("Z coordinate：",Z)
    #print("Time：",T)
    #print("Travel time of the last period：",t_n,"Initial velocity of the last period：",V_z[i])
    #print("Initrial velocity, Travel time：",V_z,T_crash)

    return z_t

if __name__ == "__main__":
    pos_x = -311.5
    #position = np.loadtxt('test2_data.csv',delimiter=',')
    #start = 48
    #end = 57
    X_matrix =[-199.5,-218.5,-235.5]
    Z_matrix =[-27,-58.5,-98.5]

    print("Predicted z coordinate：",side_view_prediction(X_matrix,Z_matrix,pos_x))







