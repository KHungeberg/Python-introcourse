# Introduction to working with files and working directory. 
import math as ma
import numpy as np
import os # os gives us a variety of functions which can print and or display the documents in you working directory
# It can also change the working directory, which 

# UNCOMMENT LINE 8 - 30.
# print(os.getcwd()) #This prints the current working directory

# print(os.listdir(os.getcwd())) # This prints out all the files in your current directory. 

# # We can also create new files within 

# x = np.arange(1,10)

# y = np.sin(x)

# np.savez("saved.npz",x=x,y=y) #Saves our variables in a file called saved.npz. if you load this script 2 times, a file called 
# # "saved.npz" should appear because of line 9. 

# del x # deletes variable x
# del y # deletes variable y

# tmp = np.load("saved.npz") #Loads the new file 

# x=tmp["x"] # 

# y = tmp["y"]

# print(x)

print(np.array([[1,2,3],[4,5,6]]))

# EXERCISES 

# EXERCISE 6A

# 1 ) Change the current working directory to the place where you have saved the file

# ANSWER) The file is saved in my working directory 

# 2 ) List the content of the working directory to check that the file is there 

# ANSWER:

print(os.listdir(os.getcwd()))

# 3 ) Load the file into Python such that the two variables are called x and y.

L = np.load("smooth.npz")

x = L["x"]

y = L["y"]

# 4 ) Plot the content of the variable x and y. It should look roughly like an inverted U-shape

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()

y = 1-y

np.savez("smooth.npz",x=x,y=y)

