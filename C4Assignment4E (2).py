# Assignment 4E: Bacteria growth: 
import numpy as np
import math as ma
# Write a program that simulates the bacteria growth hour by hour and stops when the number of bacteria exceeds
# some fixed number, N. Your program must return the time t at which the population first exceeds N. Even
# though the actual number of bacteria is really a whole number (integer) your program must work with nt as a
# decimal number (real), i.e., you should not round the numbers

# The number of bacteria at n+1 is best approximated by the formula: 
    
    # n(t+1)=(1+alpha*(1-n(t)/K))*nt

# In function we'll have 4 inputs:
    
    #a0=Number of bacteria at t=0
    #alpha=out population growth coefficient. 
    #K=capacity(maximal number of bacteria possible)
    #N=Final pupulationsize 

def bacteriaGrowth(n0,alpha,K,N):
    tN = n0
    t = 0
    while tN < N:
        tN = (1+alpha*(1-tN/K))*tN
        t = t+1
    return t

print(bacteriaGrowth(100.0, 0.4, 1000.0, 500.0))
        
