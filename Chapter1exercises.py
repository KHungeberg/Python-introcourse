# Exercises of Chapter 1 in the course "introduction to python programming and data processing. 

# EXERCISE 1A Getting to know the interface: 

# 1) Click with the mouse in the console window. Type a = 3 and press enter. You have now prompted
# Python to create a variable called a, and given it the initial value 3. Notice that the variable a is now
# shown in the variable explorer window.

# Answer: This has created an integer variable with the value 3 

# 2) Type a+2 in the console window and press enter. Python now shows the result of the arithmetic operation
# of adding 2 to the value of a. Notice in the variable explorer window that the value of a is unchanged.

# Answer: Typing this into the console returned the value 5 and a remains unchanged: 
    
# 3) Type a = a + 2 and press enter. This instructs Python to perform the arithmetic operation and write
# the result to the variable a.

# What is the variable value of a now?: 

# Answer: The value of a has now changed to 5. 

# 4) Use the console window to make the following variables: 
    # x with the value 4 
    # y with the value 7
    # z with the value of x+y 
    # Check that the value of z is 11
    
    # Answer: the valu of z is indeed 11. 

# 5) Type in the seqeuence a=7,b=a,a=9. What will the value of b be and why?:
    
    # Answer: The value of b will remain as 7 since we assigned a the value of 9 after creating b. 

# EXERCISE 1B Simple arithmetic operations:

# 1) What are the results of the following expressions? Think about it first, then type the expressions in the
# console window to verify.
# 9 / 2 + 2
# 6 + 4 * 4
# 4 / 6 + 2
# 2 - 3 * 2 - 4
# (7 - 5) * (7 + 5)
# (3 * (4 - 2 * (3) + 4))

# Answer: Writing this into the console window returns (in the same order af above):
    # 6.5
    # 20
    # 2.666...5
    # -8
    # 24
    # 6

# 2) The exponentiation operator in Python is **. What do you expect the results of the following expressions
# to be? Verify, by writing the expressions in the console window.

# 2**3
# 3**2 - 4**2
# 2**2**3
# 2**(2**3)

# Answer: This returns: 
    # 8 
    # -7
    # 256
    # 256

# 3) Verify in python that the following expressions are correct: 
    # A sequence of equations are displayed and would in python look like: 
        # 3*(2+3**2)=33
        # 4**2+3**3+2**4+1=60
        # 1/(1/2+1/3+1/6)=1
    
    # Answer: These are indeed true, however the last equations returns 1.000...2 which can be expected since 
    # python cannot comput infinite decimal places. 


# EXERCISE 1C Help on functions:

# Her we import the math package: 
    
import math 

# 1) Use the help to confirm that the function calculates and returns the sine of an angle in radians and not
# in degrees.
# Next, test this in the console window by writing both of the following lines and inspecting the results:
    # math.sin(0.5*math.pi)
    # math.sin(90)

# Answer: 
    # sin(0.5*pi) is indeed 1 (measured in radians)
    # sin(90) is indeed 0.89399... 

# 2) Use the help to examine what the functions round, math.floor, math.ceil, and math.trunc do.
# Next, verify your findings by answering the following questions:
# • Is math.floor(2.5) the same as math.trunc(2.5)?
# • Is math.ceil(-3.6) the same as math.trunc(-3.2)?
# • Is round(3.4) the same as math.ceil(3.4)?
# • Is round(-3.4) the same as math.ceil(-3.4)?

# Answer: I will answer the questions by the same order: 
    # 1: They return the same value, but the functions do not do the same though similar (what integral?)
    # 2: They return the same value of -3. Still not the same function though 
    # 3: They do not return the same value as rounding af number with decimals off to the closest integer 
    # is not the same as returning the closest integer >=x
    # 4: They return the same now, since the closest integer is also the closest integer >=-3.4

# 3) The round function can also take a second argument, specifying how many decimal places to round off
# to. Try using this to round of the number 1234.56789 to the following values

# • 1234.568
# • 1234.6
# • 1235
# • 1200

# Answer: To return those values i've written in the same order as above:
    # round(1234.56789,3)
    # round(1234.56789,1)
    # round(1234.56789,0)
    # round(1234.56789,-2)


# 4) The function math.log can be used to compute the logarithm of a number. There exists different logarithm
# functions with different base, such as the base-10 logarithm and the natural logarithm where the base is
# Euler’s number, e. Use the help to find out what the base is in the math.log function.

# Answer: The math.log function is the natural log with base e. 

# Exercise 1D Mathematical functions:
    
# 1) Write the following lines in the console window and observe what they do:
# math.pi
# math.sqrt(25)

# Answer: they return pi to 16 decimal places and 5.0

# 1.2)  The radius of a circle kan be found when you know the area by:
    # r=sqrt(A/pi) where A is the Area of the circle, how can you calculate r when A=30? 

# Answer: by using the sqrt and pi from the math package:
    # A = 30
    # r = math.sqrt(A/math.pi) 
    # r = 3.09...

# 2) Type a = 51 and press enter. Now the variable a contains the value 51. Type b = math.log(a) to get
# Python to compute the logarithm of 51. What do the variables a and b contain now?
# Next, type a = "fiftyone". Again, type b = math.log(a). This time you will get an error message—
# why? Confirm that since the command failed, the variable b whas not changed.

# Answer: Yes, the value of b has not changed since we tried to take the log of a string. 

# Exercise 1E Scripts:
    
# • Create a new empty file in the editor window.

# • In the empty file, write the three commands you used to solve exercise 1A part 4.

# • Save your script (for instance as myFirstScript.py). Notice that the script is now listed in the file explorer
# window.

# • Execute the commands in your script. This can be done by pressing F5 from within the editor.

# • Save your script under a different name, and observe that both script-files are now present in the file
# explorer window. 

# Answer: No real answer to this one. I've created the new file and it came up. 

 









