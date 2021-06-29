# CHAPTER 4 ASSIGNMENT 4D: FERMANTATION RATE 
import math as ma
import numpy as np
# When a nutrient solution is seeded with yeast, the yeast will grow and ferment sugar into alcohol and carbon
# dioxide. You are conducting a series of experiments to determine the rate of fermentation, r, 
# and have measurements of the fermentation rate measured in gram
# liter·day for a large number of identical experiments. To get a precise
# estimate of the fermentation rate, you want to compute the average of all the measured rates; however, you
# notice that some of the measurements are clearly erroneous. You decide to exclude all invalid measurements,
# which you define as measurements that are outside the range L < r < U.

# Write a program that computes and returns the mean fermentation rate, taking only the valid measurements
# into account.

# We want to define a loop that takes in 3 inputs, a vector of measurements(data), a a lower bound and 
# an upper bound. 

def fermentationRate(measuredRate,lowerBound,upperBound):
    k=0
    A=0
    for i in range(np.size(measuredRate)):
        if (measuredRate[i]> lowerBound) and (measuredRate[i]<upperBound):
            A = A+measuredRate[i]
        else:
            k = k+1
    return A/(np.size(measuredRate)-k)
            

