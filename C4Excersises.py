# CHAPTER 4 EXERCISES 
import math as ma
import numpy as np
# EXERCISE 4A: Repeated printing.

# 1.Write a script that prints I love programming! 10 times.
# 2. Write a script that uses a for-loop to print a sequence of numbers, x1 to x10, where x1 = 2 and the
# subsequent numbers are computed as xi = 2 · x_{i−1}. Check that your program prints the sequence
# 2 4 8 16 32 64 128 256 512 1024.
# 3. Write a script uses a for loop to print out the following:
# The square root of 1 is 1.0000
# The square root of 2 is 1.4142
# The square root of 3 is 1.7321
# ...
# The square root of 10 is 3.1623
# Make sure that the square roots are printed with four decimals.
# 4. Write a script that uses a loop to print
# The train will leave at 13:36 tomorrow
# The train will leave at 13:56 tomorrow
# The train will leave at 14:16 tomorrow
# ...
# The train will leave at 17:16 tomorrow
# You may assume that trains leave every 20 minutes.

# ANSWERS:

# 1)

# for i in range(10):
#     print("I love programming!")

# # 2) for every iteration 2 is multiplied with again and again, so it's basically the exponential sequence. 
# for i in range(10):
#     A = 2**(i+1)
#     print(A)

# 3) 

# for i in range(1,11):
#     print("The square root of",i,"is",round(ma.sqrt(i),4))

# 4)
# start = 13.36
# while start<17.16:
#     if (start-ma.floor(start))<0.60:
#         print("The train will leave at", round(start,2),"tomorrow")
#     else:
#         print("The train will leave at",round(start+1-0.60,2), "tomorrow" )
#     start = start + 0.20

# Excercise 4B: Power series approximation 

# Pi can be approximated by the power series (4\cdot \sum_{n=0}^N\frac{(-1)^n}{2n+1})

# Write a script that approximates pi by evaluating the equation above with N = 100.
# 1. Write the script using a for-loop.
# 2. Write the script using vectorized computation.

# k = np.ones(101) # Here we create a sample vector to contain values. 
# for i in range(101):
#     k[i] = (((-1)**i)/(2*i+1))
#     if i==100:
#         print(sum(4*k))

# Exercise 4C: Square roots

# Take a number a. If we want to find the square root of this number, such that x=sqrt(a)
# we first start with x = a/2, then x1=(x+(a/x))/2 and the x2 is the an iteration of the first step and so on

# Write a program that approximates the square root as described above. How many updates are required to get
# the first five significant digits correct when approximating p2?

# Using vectorized computation we can solve this as such: 
# def approx(a,k):
#     p=np.ones(k)
#     for i in range(np.size(p)):
#         if i==0:
#             p[i] = a/2
#         else:
#             p[i] = (p[i-1]+(a/(p[i-1])))/2
#     return p[np.size(p)-1]

# # Checking the number of iterations needed before the first 5 significant digits are there. 
# k = 1
# while round(approx(2,k),5) != round(ma.sqrt(2),5):
#     print(k, "is not enought iterations, try", k+1,"iterations")
#     k = k+1

