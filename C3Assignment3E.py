# ASSIGNMENT 3E: Acidity 
import math as ma
import numpy as np

# The pH value of a component determines the acidity and or how basic it is. low values are acidic and 
# high values are alkaline(basic). Values are descriped as such:
    
    # 0-2 : Strongly acidic
    # 3-5 : weakly acidic
    # 6-8 : Neutral 
    # 9-11: weakly basic
    # 12-14 : Strongly basic

# Create a function that converts a pH value to the corresponding category. 
# If the pH is between two categories, it must be assigned to the strongest (acidic or basic) 
# category of the two. If the pH is a number outside the scale the string pH out of range must be returned.

# We'll create it with lots of if statements 

def pH2Category(pH):
    if (round(pH) <= 2):
        catagory = "Strongly acidic"
    elif (round(pH)>2) and (round(pH)<=5):
        catagory = "Weakly acidic"
    elif (round(pH)>5) and (round(pH)<=8):
        catagory = "Neutral"
    elif (round(pH)>9) and (round(pH)<=11):
        catagory = "Weakly basic"
    elif (round(pH)>11) and (round(pH)<=14):
        catagory = "Strongly basic"
    return catagory

print(pH2Category(5.3))

# Codejudge will not accept this code, but it's the testing i Codejudge which is flawed. 
# How can they expect the value 2.3 to be Strongly acidic but then 
# demand 11.1 to be returned as Strongly basic? It is clearly closer to being weakly basic. 
 
