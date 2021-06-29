# C6 ASSIGNMENT 6E
import math as ma
import numpy as np
import pandas as pd
# Create a function that takes as input a vector of frequencies of occurrences of letters in a text. The function
# must read the file letter_frequencies.csv, compute the squared error for each language, and return a vector
# of squared errors for the fifteen languages

# Our method here is that, since we have rows in both the freq variable and in the vectorized version of 
# the CSV file, we can column by column (language by language) take the square distance between the two
# Thereafter we take the column sum which gives us our desired output. 

def computeLanguageError(freq):
    letterfreq = pd.read_csv("letter_frequencies.csv")
    vecletterfreq = np.array(letterfreq)
    for i in range(16):
        if i==0:
            vecletterfreq[:,i]=vecletterfreq[:,i]
        else:
            vecletterfreq[:,i]=(freq-vecletterfreq[:,i])**2
    se = np.sum(vecletterfreq[:,1:16],axis=0)
    return se

    
    