# C5 EXCERSISES
import numpy as np
import math as ma
# EXERCISE 5B

# Write a script, that interacts with the user to convert a temperature from one unit to another. Make use of the
# function you implemented in assignment 5A. The program flow must be as follows:
# 1. The user is prompted to input a temperature (a decimal number).
# 2. The user is prompted to input the unit of the temperature (a string).
# 3. The user is prompted to input the unit of the temperature (a string) to convert to.
# 4. The program displays the converted temperature.
# A session where the user interacts with the program might look as follows. The input given by the user is
# highlighted with red (the text should not be colored in your program.)

# def convertTemperature(T, unitFrom, unitTo):
#     f = np.copy(T)
#     if unitFrom=="Fahrenheit" and unitTo=="Celsius":
#         T = (T-32)/1.8
#     elif unitFrom=="Fahrenheit" and unitTo=="Kelvin":
#         T = (T+459.67)/1.8
#     elif unitFrom=="Celsius" and unitTo=="Kelvin":
#         T = T+273.15
#     elif unitFrom=="Celsius" and unitTo=="Fahrenheit":
#         T = 1.8*T+32
#     elif unitFrom=="Kelvin" and unitTo=="Fahrenheit":
#         T = 1.8*T-459.67
#     elif unitFrom=="Kelvin" and unitTo=="Celsius":
#         T = T-273.15
#     return print(f,unitFrom,"=",T,unitTo)

# In this section we define our temperature and units. the function 'try' will test the input, so for example if 
# u input a string as T, you will get a valueError wich will tell the program to print an errormessage. This is done 
# likewise with the other variables. In the end 

# while True:
#     try:
#         T = float(input("Please input a temperature "))
#         break
#     except ValueError:
#         print("Wrong input, numerical answers only")
# while True:
#     try:
#         unitFrom = str(input("Please input the unit of temperature "))
#         break
#     except ValueError:
#         print("Not valid format")
# while True:
#     try:
#         unitTo = str(input("Please input the unit to convert to "))
#         break
#     except ValueError:
#         print("not valid format")
        
# print(convertTemperature(T, unitFrom, unitTo))

# Discussion and further analysis: 
    
# How could you modify the code to be insensitive to capital letters? 

# I could change the definition of the function to be defined by the lowercase spelling of the temperaturen and then
# change the input with .lower() so no matter how i write the unit in terms of lower and upper case letters, the program 
# will change it only lowercase so the function can interpret the input properly. 

# Also allow the user to just type C,F or K: 

# I could change the definition of the function with an "or" statement. Or maybe start with a lot of if statements with 
# if unitFrom == "K":
    # unitFROM == "Kelvin"

# EXCERCISE 5C

# In interactive computer programs it is sometimes useful to ask the user to choose between different options by
# displaying a simple menu. The following function, which uses the function inputNumber discussed previously,
# displays a menu and returns the number of the chosen menu item

# First we implement the function inputNumber within our own function here, so that we can use it within. 
# Then we define our menu 
# def displayMenu(options):
#     def inputNumber(prompt):
#         while True:
#             try:
#                 num = float(input(prompt))
#                 break
#             except ValueError:
#                 pass
#         return num
#     for i in range(len(options)):
#         print("{:d}. {:s}".format(i+1, options[i])) 
#     choice=0
#     while not(np.any(choice == np.arange(len(options))+1)):
#         choice = inputNumber("Please choose a menu item: ")   
#     return choice

# displayMenu(np.array(["carrot","pasta","bread"]))
# Examine the function to figure out how it works, and try it out (you can simply copy-paste it into Python).
# Remember that it uses the inputNumber function discussed previously, so you need to have that in place also.

# EXCERCISE 5D:
    
# We want to generate uniformly distributed random numbers, where the mean of the distribution given by μ
# and the width of the distribution is given by R. Thus, the uniform random number must be on the interval
# [mu-R/2,mu+R/2]. Although the mean of the distribution is equal to μ, if you generate, say, ten random numbers
# from this distribution it is not guaranteed that the empirical mean (the average) of the generated numbers will
# be equal to μ. In this exercise, we will investigate this futher.

# Implement a function randomSequence that returns a sequence of N random numbers on the range described
# above, where μ, R and N are given as parameters to the function.
# Write a script that does the following:
# 1. Use the function randomSequence to generate a vector of random numbers.
# 2. Calculate the empirical mean of the returned vector.

# We want to create a random sequence of numbers between the given interval. This we can do by using the np.random.rand()
# function which gives us random real numbers between 0 and 1. from the given interval we recognize the lower and upper 
# bound. 

# if r is a random number in the interval [0;1], we can generate a random number between lowerbound l and upperbound u as 
# such r*=(u-l)*r+l

def randomSequence(mu,R,N):
    Q = R*(np.random.rand(N))+mu-R/2
    return Q

print(np.mean(randomSequence(6, 25, 10000)))

# Discussion for further analysis

#   How does the empirical mean relate to the theoretical mean for different values of N (like 10, 100, 1000)?:
    
    # Answer: The mean gets closer and closer the bigger N gets. However, it depends on the variance (distance from the mean)

# • How does the empirical means compare for multiple runs with the same N?:
    
    # Answer: It hits close with a variance that gets smaller the bigger N gets. 
    
# • How could you empirically estimate the range?:
    
    # I could use a very large N and use the np.max and np.min function. 
    




