# ASSIGNMENT 4F: REMOVING INCOMPLETE EXPERIMENTS: 
import math as ma
import numpy as np
# You are working on a data set from a series of experiments, each of which consists of three parts. The experiments
# have been performed in a randomized order. Each experiment has been assigned an experiment-number and
# a part-number, which are joined into one decimal number called an id-number. The id-number is formed by
# separating the experiment-number and part-number by a decimal point. For example, the experiment number
# 17 part 3 has been assigned the id-number 17.3. Note, that you can compute the experiment-number from the
# id-number by rounding down to the nearest integer.
# You notice that due to errors, for some of the experiments all three parts have not been completed. For further
# analysis, you need to exclude all experiments where one or more parts are not available. You can safely assume
# that if there are 3 id-numbers with the same experiment-number, the experiment is complete.

# Create a function that takes as an input a vector of id-numbers and returns a vector of id-numbers where all
# incomplete experiments have been removed. The id-numbers that are not removed must remain in the same
# order as in the original vector.

# Let's use the round and np.round function since the decimals only go up to 3, it will always be rounded down to 
# the experiment number. Thus, the experiment number should appear 3 times in the rounded vector. We then use this to 
# our advantage to make a logical if statement. If the experiment number appears 3 times in the rounded vector, we let the 
# i'th element stay and if not, we turn it into a number which most likely will not appear in the original vector (x). 

def removeIncomplete(x):
    for i in range(np.size(x)):
        l = round(x[i])
        if 3 == np.size(np.round(x)[np.round(x)==l]):
            x[i] = x[i]
        else:
            x[i] = 19187429623424
    return x[x!=19187429623424]
        
            
print(removeIncomplete(np.array([1.3, 2.2, 2.3, 4.2, 5.1,
3.2, 5.3, 3.3, 2.1, 1.1, 5.2, 3.1]))) # Prints out the solution with this vector. 