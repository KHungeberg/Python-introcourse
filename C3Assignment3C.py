#ASSIGNMENT 3C

# Write a function that takes as input two unit vectors v1 and v2 representing two lines, and computes the acute
# angle between the lines measured in radians. 

# First we import math and numpy 

import math as m
import numpy as np

# The formula for calculating the angle between 2 unitvectors is arrccos of the dot product of the vectors. 

# We define out function as such:

def acuteAngle(v1,v2):
    if m.acos(np.dot(v1,v2))>(m.pi/2):
        theta = m.pi - m.acos(np.dot(v1,v2))
    else:
        theta =  m.acos(np.dot(v1,v2))
    return theta


print(acuteAngle(np.array([(-4.0)/5.0,3.0/5.0]),np.array([(20.0)/(29.0),(21.0)/(29.0)]))) #Test of function. 