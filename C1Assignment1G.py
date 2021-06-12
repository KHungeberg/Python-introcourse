# ASSIGNMENT 1G

import math as m

# The cosine rule can be used to compute the length of a side in a triangle (a), when you know the other two
# sides (b, and c) and the opposing angle (A):

# Create a script that carries out the following steps:
# 1. Create a variable b and set it to 12.
# 2. Create a variable c and set it to 10.
# 3. Create a variable A and set it to 0.25*pi.
# 4. Compute the length of the side a using the cosine rule.
# • Save the solution in a variable a.

b = 12
c = 10
A = m.pi*0.25

a = m.sqrt(b**2+c**2-2*b*c*m.cos(A))

print(a)
