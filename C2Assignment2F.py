#ASSIGNMENT 2F: PROJECTION 

# Create a function named computeProjection that computes the projection of the vector b = [1, 1, . . . ] onto
# the vector a which is taken as an input to the function. The output must be the projection p. Note that b is
# a vector with all elements equal to one and with the same dimensions as a, and that the function should work
# for vectors of any dimensionality.

import numpy as np

# Now we compute the function 

# let us remember the projection is the dot product of a and b over the squared norm of a, all multiplied on a 

def computeProjection(x):
 return (np.dot(x,np.ones(np.size(x)))/(np.dot(x,x)))*x

# Input a vector of any dimension and this function will calculate the projected vector projected onto the 
# vector of the same dimension with 1 in every entrance. 





