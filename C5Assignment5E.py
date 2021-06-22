# CHAPTER 5 ASSIGNMENT MONTE CARLO PROBLEM
import numpy as np
import math as ma
# We can approximate the area of af circle within a square by multiplying the area of the rectangle by the fraction of 
# randomly positioned points within the circle and total points within the square. 

# A_c \approx (A_s*n)/N

# Well assume the circle is placed in origo and has a radius equal to 1 and is positioned within a square hitting 
# the periphery of the circle. 

# Problem definition
# Write a function that estimates the area of a circle by Monte Carlo simulation. As input the function must
# receive two vectors containing the coordinates of the randomly drawn points. The function must return the
# estimated value of the area as output.
# To test your function, you can use the function implemented in exercise 5D to generate a vector for the random
# x-values and a vector for the random y-values.

# Solution thoughts: Well use the function generation random number generator we made in Exercise 5D and then well set the
# total number of points as the size of the input vectors. Since we are assuming we are within the square, well use mu=0
# and R=1. To calculate which points are within the circle, well use the euclidian norm of the vectors from origo to 
# the points within the square. If it is less than og equal to 1 we know it is within the circle, if not, it is out of the 
# circle. 
def randomSequence(mu,R,N):
        Q = R*(np.random.rand(N))+mu-R/2
        return Q
xvals = randomSequence(0, 2, 1000)
yvals = randomSequence(0, 2, 1000)

def circleAreaMC(xvals,yvals):
    n = 0
    for i in range(np.size(xvals)):
        if ((xvals[i])**2+(yvals[i])**2)<=1:
            n = n+1
    A = (4*n)/np.size(xvals)
    return A

print(circleAreaMC(xvals, yvals))
            
    
    


