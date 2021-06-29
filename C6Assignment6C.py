# ASSIGNMENT 6C
import numpy as np
import math as ma
# Create a function that takes a signal vector as input and computes the five-sample weighted moving average of
# the signal.

# The weighted average can be calculated with the formula below: 
    
# yhat_i = \frac{y_{i-2}+2*y_{i-1}+3*y_i+2*y_{i+1}+y_{i+2}}{9}

# if i=2 or N-2, then we let y_{i+2}=0 and likewise for N-2. 

def movingAvg(y):
    N = np.size(y)
    if N==1:
        ysmooth = y[0]/3
    else:
        for i in range(N):
            if i==0:
                ymat = np.array([0,0,3*y[i],2*y[i+1],y[i+2]])
            elif i==1:
                    ymat = np.vstack((ymat,[0,2*y[i-1],3*y[i],2*y[i+1],y[i+2]]))
            elif i==(N-2):
                ymat = np.vstack((ymat,[y[i-2],2*y[i-1],3*y[i],2*y[i+1],0]))
            elif i==(N-1):
                ymat = np.vstack((ymat,[y[i-2],2*y[i-1],3*y[i],0,0]))
            else:
                ymat = np.vstack((ymat,[y[i-2],2*y[i-1],3*y[i],2*y[i+1],y[i+2]]))        
        ysmooth = np.sum(ymat,axis=1)/9

    return ysmooth

print(movingAvg(np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])))
