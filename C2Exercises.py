# CHAPTER 2 EXCERCISES
import numpy as np
import math as ma
# Exercise 2B

# Use the appropriate vector initialization functions and operators to create the following vectors:
# 1. v1 = [3, 7, 1] (Hint: Use direct assignment)
# 2. v2 = [0, 0, 0, 0, 0, 0] (Hint: Use np.zeros)
# 3. v3 = [1, 1, 1]
# 4. v4 = [1, 2, 3, 4]
# 5. v5 = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
# Use appropriate methods to access the vectors to answer the following questions:
# 1. Access the first element of the v1 vector.
# 2. Access the second element of the v4 vector.
# 3. What happens if you try to access the fourth element of vector v3.
# 4. How can you change vector v4 to store 10 as the fifth element?
# 5. How can you change the vector v5 so that it becomes equal to [3, 7, 1]?

# Answer: I Answer in the same order as above: 
    
# 1.1) 

v1 = np.array([3,7,1])

# 1.2) 

v2 = np.zeros(6)

# 1.3)
v3 = np.ones(3)

# 1.4)

v4 = np.arange(1,5) # Remember the np.arange work a bit like the semicolon operator in R.

# 1.5) 

v5 = np.arange(1,15)

# 2.1)

print(v1[0])

# 2.2)

print(v4[1])

# 2.3) 

# v3[3] # out of bounds error. 

# 2.4) 

v4 = np.concatenate((v4,np.array([10]))) 

# 2.5) 

v5 = v1

# EXERCISE 2C: vector operations:
    

# Create the vectors v1 = [1, 2, 3, 4, 5], v2 = [3, 4, 5, 6, 7], and v3 = [1, 1, 1, 1]. Create a script 
# that outputs the following:
# 1. The dot product of v1 and v2.
# v1 · v2 = 1 · 3 + 2 · 4 + 3 · 6 + 4 · 7 + 5 · 8 = 85.
# 2. Element-wise multiplication of v1 and v2.
# [1 · 3, 2 · 4, 3 · 6, 4 · 7, 5 · 8] = [3, 8, 15, 24, 35].
# 3. The sine function applied to each element in v1.
# sin(v1) = [0.8415, 0.9093, 0.1411,−0.7568,−0.9589].
# 4. The length of v1 which is 5.
# 5. The dot product of v1 and v3.
# (Hint: What happens when you try to compute this?)

# Answer: Solving same sequence as above: 
    
v1 = np.arange(1,6)
v2 = np.arange(3,8)
v3 = np.ones(4)

# 1) 

print(np.dot(v1,v2))

# 2) 

print(v1*v2)

# 3) Remember here that ma.sin takes singular value input, so no vectors. Use np.sin instead. 

print(np.sin(v1))

# 4) here we can use the len(x) function in base python or np.size from numpy

print(np.size(v1))

# 5) 

# print(np.dot(v1,v3)) Dimension error. 

# EXERCISE 2D: logical vector indexing. 

# Create the vectors v1 = [4, 2, 1, 2, 5] and v2 = [−1, 4, 5,−3, 6]. Use logical indexing to compute a new vector v3
# containing the following:
# 1. The elements of v1 that are less than 3. (v3 = [2, 1, 2])
# 2. The elements of v2 that are negative. (v3 = [−1,−3])
# 3. The elements of v2 that are greater than 0. (v3 = [4, 5, 6]).
# 4. The elements of v1 that are greater than 100. There are none, so what happens?
# 5. The elements of v1 that are greater than the corresponding element in v2. (v3 = [4, 2])
# 6. The elements of v2 that are not equal to 5. (v3 = [−1, 4,−3, 6])
# 7. The elements of v1 that are greater than the average of the elements in v1. (v3 = [4, 5])

v1 = np.array([4,2,1,2,5])
v2 = np.array([-1,4,5,-3,6])

# Answer (in same sequence as above)

# 1) 

print(v1[v1<3])

# 2) 

print(v2[v2<0])

# 3) 

print(v2[v2>0])

# 4) 

print(v1[v1>100]) # Returns an empty vector. 

# 5) 

print(v1[v1>v2])

# 6) 

print(v2[v2 != 5])

# 7)

print(v1[v1>np.mean(v1)])

#EXERCISE 2E: Modifying vectors: 
    
# Consider the vector v = [4, 7,−2, 9, 3,−6,−4, 1]. Which Python command will do the following:
# 1. Set all negative values to zero. (v = [4, 7, 0, 9, 3, 0, 0, 1])
# 2. Change the sign of all values. (v = [−4,−7, 2,−9,−3, 6, 4,−1])
# 3. Set all values that are less than the average to zeros. v = [4, 7, 0, 9, 3, 0, 0, 0]
# 4. Set all negative values to positive. (v = [4, 7, 2, 9, 3, 6, 4, 1])
# 5. Multiply all positive values by two. (v = [8, 14,−2, 18, 6,−6,−4, 2])
# 6. Raise all values to the power of 2, but keep their original sign. (v = [16, 49,−4, 81, 9,−36,−16, 1])

v = np.array([4,7,-2,9,3,-6,-4,1])

# 1) The command: v[v<0]=0 

# 2) Simply multiplying the vector by -1 so the "command" -v 

# 3) the command: v[v<np.mean(v)]=0

# 4) the command: v[v<0] = -v[v<0]

# 5) the command: 2*v

# 6) the command: v[v>0] = v[v>0]**2 followed by v[v<0] = v[v<0]**2


