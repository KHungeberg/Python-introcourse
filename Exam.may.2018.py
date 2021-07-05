# EXAM SET MAY 2018
import numpy as np
import math as ma
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
# ASSIGNMENT A SPACE WEIGHT: 
    
# Create a function named weightOnPlanet that takes as input the weight of a person on earth, and a planet
# number from the table above. The function must return the weight of the person on that planet.  

def weightOnPlanet(weight,planetNumber):
    if planetNumber==1:
        newWeight = weight*0.91
    elif planetNumber==2:
        newWeight = weight*0.38
    elif planetNumber==3:
        newWeight = weight*2.53
    elif planetNumber==4:
        newWeight = weight*1.06
    elif planetNumber==5:
        newWeight = weight*0.89
    elif planetNumber==6:
        newWeight = weight*1.13
    return newWeight

print(weightOnPlanet(85,5))

# ASSIGNMENT B PLANET CLASSIFICATION 

# Create a function named planets that takes as input a vector of
# numbers between 1 and 5, corresponding to a list of planet categories.
# The function must return an array of strings that contains the names of the planets that belong to
# one or more of the input categories. The order of the planet names must be as in the figure, and the planet
# names must be written with the first letter capitalized as in the figure.

def planets(planetCatagories):
    planetNames = [""]
    planetCatagories = np.sort(planetCatagories)
    planorder = np.array(["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"])
    for i in range(np.size(planetCatagories)):
        if planetCatagories[i]==1:
            planetNames = np.concatenate((planetNames,planorder[0:4]))
        elif planetCatagories[i]==2:
            planetNames= np.concatenate((planetNames,planorder[0:2]))
        elif planetCatagories[i]==3:
           planetNames = np.concatenate((planetNames,planorder[3:9]))
        elif planetCatagories[i]==4:
            planetNames = np.concatenate((planetNames,planorder[4:9]))
        elif planetCatagories[i]==5:
            planetNames = np.concatenate((planetNames,planorder[4:8]))
    for j in range(np.size(planetNames)):
        for k in range(np.size(planetNames)):
            if (planetNames[j]==planetNames[k]) and (j != k):
                planetNames[k] = ""
    return planetNames[planetNames != ""]

# print(planets(np.array([4,2,5])))

# ASSIGNMENT C 15-PUZZLE

# Create a function named inversions that takes as input a vector containing 15 numbers (integers 1–15)
# corresponding to a configuration of a board for a game of 15-puzzle taken row by row. The function must
# return the number of inversions in the position

def inversions(board):
    k = 0
    for i in range(np.size(board)-1):
        if board[i]>board[i+1]:
            k = k+1
    return k

# ASSIGNMENT D POLYGON CONVEXITY CHECK

# Create a function named polygon that takes as input two vectors containing the x- and y-coordinates
# respectively, and returns the values c1, c2, . . . , cn as a vector.

def polygon(x,y):
    C = np.ones(np.size(y))
    for i in range(np.size(x)):
        if i < (np.size(x)-2):
            C[i] = (x[i]-x[i-1])*(y[i+1]-y[i])-(x[i+1]-x[i])*(y[i]-y[i-1])
        elif i == (np.size(x)-2):
            C[i] = (x[i]-x[i-1])*(y[i+1]-y[i])-(x[i+1]-x[i])*(y[i]-y[i-1])
        elif i == (np.size(x)-1):
            C[i] = (x[i]-x[i-1])*(y[0]-y[i])-(x[0]-x[i])*(y[i]-y[i-1])
    return C
    
x1 = np.array([1,3,3,4,7,6,1])

y1 = np.array([1,1,2,3,3,5,5])

print(polygon(x1, y1))
        
# ASSIGNMENT E MEDALS

# Create a function named medal that takes as input an string representing one of the four age groups, as
# well as a point score. The function must only consider the first character in the input-string that defines
# the age group (i.e. B, P, G, or T). The function must return a text string which depends on which medal (if
# any) the participant has won.
# If the participant has won a medal, the return value must be on the following form:
# You got <pts> points and won a <mdl> medal.
# Otherwise, if the participant did not win a medal, the return value must be on the following form:
# You got <pts> points.
# In these return values, the placeholders <pts> and <mdl> must respectively be replaced by the number of
# points and the type of medal (gold, silver, or bronze).
import numpy as np
def medal(ageGroup,points):
    prize = np.array(["bronze","silver","gold","no medal"])
    life = np.array(["Baby","Preschooler","Gradeschooler","Teen"])
    lifeL = np.array(["B","P","G","T"])
    for i in range(4):
        if life[i]==ageGroup:
            ageGroup = lifeL[i]
    if ageGroup=="B":
        if points in np.arange(0,5):
            prize = prize[0]
        elif points in np.arange(5,10):
            prize = prize[1]
        elif points in np.arange(10,21):
            prize = prize[2]
        else:
            prize = prize[3]
    elif ageGroup=="P":
        if points in np.arange(5,10):
            prize = prize[0]
        elif points in np.arange(10,15):
            prize = prize[1]
        elif points in np.arange(15,21):
            prize = prize[2]
        else:
            prize = prize[3]
    elif ageGroup=="G":
        if points in np.arange(11,14):
            prize = prize[0]
        elif points in np.arange(14,17):
            prize = prize[1]
        elif points in np.arange(17,21):
            prize = prize[2]
        else:
            prize = prize[3]
    elif ageGroup=="T":
        if points in np.arange(15,17):
            prize = prize[0]
        elif points in np.arange(17,19):
            prize = prize[1]
        elif points in np.arange(19,21):
            prize = prize[2]
        else:
            prize = prize[3]
            
    message = print("You got",points,"points","and won a", prize,"medal.")
    return message
print(medal("P",12))