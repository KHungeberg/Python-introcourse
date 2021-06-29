# ASSIGNMENT 6D
import numpy as np
import math as ma
# Create a function that takes a text file as input and returns a vector of size 26 with the frequency in percent of
# each character a, b, . . . z (not sensitive to case.) The frequency must be computed as the number of occurences
# divided by the total number of characters from a to z that occur, multiplied by one hundred. All other letters
# such as ø and ä as well as all symbols must be ignored.

# filein = open("small_text.txt", "r") # Opens the file for reading
# lines = filein.readlines() # Reads all lines into an array
# smalltxt = "".join(lines) # Joins the lines into one big string

# for i in range(9):
#     lines[i]=lines[i].lower()

# # print(lines)

# alph = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])

# smalltxt = "".join(lines)

# ones = np.ones(1662)
# ones = str(ones)
# t = 0
# for i in range(1662):
#     if smalltxt[i] in alph:
#         t = t+1

def letterFrequency(filename):
    alph = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    filein = open(filename, "r") # Opens the file for reading
    lines = filein.readlines() # Reads all lines into an array
    smalltxt = "".join(lines) 
    freq = np.ones(np.size(alph))
    k = 0
    for i in range(np.size(lines)):
        lines[i] = lines[i].lower()   
    smalltxt = "".join(lines)
    for p in range(len(smalltxt)):
        if smalltxt[p] in alph:
            k = k+1
    for i in range(np.size(alph)):
        q = 0
        for j in range(len(smalltxt)):
            if alph[i] in smalltxt[j]:
                q = q+1
        freq[i] = (q/k)*100
    return freq
            
    
print(letterFrequency("small_text.txt"))

ex = letterFrequency(("small_text.txt"))