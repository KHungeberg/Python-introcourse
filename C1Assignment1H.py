# ASSIGNMENT 1H 

import math as m
#THE QUADRATIC FORMULA 

#The quadratic formula has the from ax^2+bx+c=0

# With the solution (-b\pm sqrt(b^2-4ac))/2a

# Create a script that carries out the following steps:
# 1. Create a variable a and set it to 2.
# 2. Create a variable b and set it to -5.
# 3. Create a variable c and set it to 2.
# 4. Compute the two solutions using the quadratic formula.
# • Save the smallest solution in a variable x1.
# • Save the largest solution in a variable x2.
# Check that your script produces the correct results, namely 0.5 and 2.

a = 2
b = -5
c = 2

x2 = (-b+m.sqrt(b**2-4*a*c))/(2*a)

x1 = (-b-m.sqrt(b**2-4*a*c))/(2*a)

