# ASSIGNMENT 6B
import numpy as np
import math as ma
# You want to compare the cost of producing some different items. To produce each item, a number of different
# resources are required. For each item you know how many units of each type of resource is required. This
# information is given as a matrix, where each column corresponds to an item and each row corresponds to a
# resource. The values in the matrix denote how many units of the resource is required for the item. Furhtermore,
# you know the cost of each resource, which is given as a vector.

# So since every column is an item and every row is a resource, if we have the cost-vector, we simply multiply the entrances 
# in the matrix by the corresponding entrances in the cost-vecktor. If we transpose the vector, we can by matrix multiplication
# get the desired outcome since it will now be the rows that are the items and the columns that are materials. 

def computeItemCost(resourceItemMatrix,resourceCost):
    itemCost = np.dot(resourceItemMatrix.T,resourceCost)
    return itemCost
    
