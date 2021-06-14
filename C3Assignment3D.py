#ASSIGNMENT 3D: Piecewise function 
import math as ma
import numpy as np
# Write a function that, given the distance x to the center of the earth,
# computes the graviational pull of theearth.

# First we write our constants. R is the approximate radius of earth (assuming the earth is a perfect sphere)
# 
R = 6.371*(10**6)

g0 = 9.82 

# Now we define our function

def gravitationalPull(x):
    if (x>=R):
        g = g0*((R**2)/(x**2))
    elif (x<R) and (0<=x):
        g = g0*(x/R)
    return g


# Uncomment this section for at the a plot of the function when it is addapted to vector values. 

# def gravitationalPull(x):
#     k = np.zeros(np.size(x))
#     for i in range(np.size(x)):
#         if (x[i]>=R):
#             k[i]= g0*((R**2)/(x[i]**2))
#         elif (x[i]<R) and (0<=x[i]):
#             k[i] = g0*(x[i]/R)
#     return k

# print(gravitationalPull(np.array([R+34,R-54,R*30])))
# What will happen if you give a vector of distances as input to your function? 
# Probably it will not work, because the function expects a single number as input. 
# How could you write the function such that it outputs a vector
# of gravitational pull when given a vector of distances as input? Think about how this could be implemented
# using vector indexing operations.
# If you change your function so that it works correctly with vector input and output, 
# you can try out making a plot of the function using the following code:

# import matplotlib.pyplot as plt
# x = np.arange(0, 10e6, 1e4)
# plt.plot(x, gravitationalPull(x))
# plt.show()