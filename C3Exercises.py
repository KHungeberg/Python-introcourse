#CHAPTER 3 EXERCISES: 
import math 
#EXERCISE 3A: True og False 

# Does each of the following bits of code print out Condition is true or Condition is false? Answer by
# looking at the code, and verify your answers with Python.
# 1.
# if math.pi < 3:
#     print('Condition is true')
# else:
#     print('Condition is false')
# # 2. 
# x = 10
# if x < 5:
#     print('Condition is true')
# else:
#     print('Condition is false')
# # 3. 
# x = 5
# if math.pi > 3 and x == 5:
#     print('Condition is true')
# else:
#     print('Condition is false')
# # 4.
# if math.pi < 3 or 5 == 5:
#     print('Condition is true')
# else:
#     print('Condition is false')
    

# Answers 

# 1) Will print Condition is false, since pi is greater than 3

# 2) Will print Condition is false since 10 is greater than 5

# 3) Will print Condition is True since pi is greater than 3 and x is equal to 5

# 4) Will print Condition is True because only one True statement is needed for an "or" condition to be True:
    # And since 5 is indeed equal to 5, it doesn't matter that pi is not smaller than 3. 
    
#EXERCISE 3B

# Evaluate the the following logical expressions 
# (note that all the expressions have the value true or false). Evaluate the expressions on paper
# or in your mind first, and then write Python code that evaluates the expression to
# verify your answers.
# 1. 9 > 3 · 3.
# 2. 9 >= 3 · 3.
# 3. (6 + 3) is equal to 3**2.
# 4. 12/5 is greater than 17/5
# 5. Either (2 is greater than 3) or (32 is not equal to 9).
# 6. 323 is not equal to (17 times 19).
# 7. The cosine of (3 times pi) is a negative number.

# Answer: I do the same as in the exercise 3A. Så i make the following if statements.:
    # Running the script should return out answer in the console

if 9>3*3:
    print("Condition 1 is True")
else: 
    print("Condition 1 is false")

if 9 >= 3*3:
    print('Condition 2 is true')
else:
    print('Condition 2 is false')

if (6+3)==3**2:
    print('Condition 3 is true')
else:
    print('Condition 3 is false')

if (12/5)>(17/5):
    print('Condition 4 is true')
else:
    print('Condition 4 is false')

if (2>3) or (30 != 9):
    print('Condition 6 is true')
else:
    print('Condition 6 is false')

if 323 != 17*19:
    print('Condition 7 is true')
else:
    print('Condition 7 is false')
