# Assignment 7G The NATO alphabet 
import numpy as np
import math as ma

# Create a function that spells out a word (written in plain text) in the NATO alphabet. The function should
# accept input in upper, lower, or mixed case, and should output the NATO “code words” exactly as written
# above, separated by dashes. You can assume that the input string contains only letters from a-z (A-Z).

def textToNato(plainText):
    alph = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    nato = np.array(["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot",
                      "Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November",
                      "Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform",
                      "Victor","Whiskey","Xray","Yankee","Zulu"])
    plainText = plainText.lower()
    natoText = ""
    for i in range(len(plainText)):
        for j in range(np.size(alph)):
            if plainText[i]==alph[j]:
                natoText = "-".join((natoText,nato[j]))
    return natoText[1:(len(natoText))]
    

print(textToNato("kanon"))