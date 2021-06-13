#ASSIGNMENT 2A TAYLOR SERIES: 
import math as m
# Create a function that returns the first 4 terms of the taylor series of the natural logarithm with x 
# as the variable and evaluatetaylor as teh name

def evaluatetaylor(x):
    return (x-1)-((x-1)**2)/2+(1/6)*((x-1)**3) 


#By uncommenting this, you can see in the console window how close we get
# print(m.log(2))
# print(evaluatetaylor(2))


# Discussion and futher analysis
# • Run the function from the console with different input.:
    
    # Answer: This returns another value similar to log of the same value. 

# • What happens when you run the function with a vector as input?:
    
    # Answer: Don't know how to make vectors in python, but probably return another vector with the function
    # values of the numbers in the vector. 
    
# • What happens when you try to run the function without input.:
    
    # Name 'x' is not defined

