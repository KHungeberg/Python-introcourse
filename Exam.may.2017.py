# EXAM MAY 2017 
import numpy as np
import math as ma

# ASSIGNMENT A SALE PRICE

# A store is having a sale and makes an offer: “Buy two and get the cheapest one for free.” You are given
# the task to implement the offer in the store’s computer system. When a customer wishes to purchase some
# number of items, the method for computing the total sale price is the following: The customer pays for the
# most expensive item, gets the second-most expensive item for free, pays for the third-most expensive item,
# gets the fourth-most expensive item for free, and so on.

# Create a function named salePrice that takes as input a vector with the prices of the items a customer
# has chosen, and computes the total sale price.
import numpy as np
def salePrice(prices):
    prices = np.sort(prices)
    for i in range(np.size(prices)):
        if np.size(prices) % 2 == 1:
            if i==0:
                prices[i]=prices[i]
            elif i % 2 ==1:
                prices[i]=0
        else:
            if i==0:
                prices[i] = 0
            elif i % 2 ==0:
                prices[i]=0
       
    return np.sum(prices)

print(salePrice(np.array([9.95,129.50,9.95,40,17.75,4,40])))
        
# ASSIGNMENT B ISBN-10 CHECK DIGIT

# Create a function named ISBNCheckDigit that takes as input a vector with the first 9 digits in an ISBN
# number and computes the check-digit as a string containing either a numeric digit 0–9 or X.           

def ISBNCheckDigit(isbn):
    vec = np.arange(1,10)
    j = np.dot(vec,isbn) % 11
    if j == 10:
        j = "X"
    return str(j)

print(ISBNCheckDigit(np.array([1,4,9,1,9,3,9,3,6])))

# ASSIGNMENT C PARTIAL CORRELATION 

# Create a function named partialCorrelation that takes as input a matrix of observations X and computes
# the matrix of partial correlations P.

def partialCorrelation(X):
    N = np.size(X[:,1])
    nX = (1/N)*(np.dot(X.T,X))
    C = np.linalg.inv(nX)
    l = np.size(C[:,0])
    k = np.ones(l)
    for t in range(l-1):
        k = np.vstack((k,np.ones(l)))
    P = k
    for j in range(np.size(C[:,0])):
        for i in range(np.size(C[0,:])):
            if i != j:
                P[i,j] = -(C[i,j])/ma.sqrt(C[i,i]*C[j,j])
            else:
                P[i,j] = 1
    return np.round(k,3)


ex = np.array([[-0.1,0.4,-1.0],[3.4,1.8,-1.0],[-1.9,-1.5,0.7],[0.8,1.6,4.4],[0.7,1.0,3.0]])

print(partialCorrelation(ex))
# ASSIGNMENT D ZERO CROSSING

# Create a function named zeroCrossing that takes as input a signal (as a vector) and returns the number
# of times the signal changes sign

def zeroCrossing(signal):
    count = 0
    for i in range(np.size(signal)-1):
        if signal[i]*signal[i+1] < 0:
            count = count +1
    return count

print(zeroCrossing(np.array([1.1,-1.3,-1.5,2.2])))

# ASSIGNMENT E RANKING PAIRWISE COMPARISON:
    
# Create a function named pairwiseRank that takes as input a matrix P of pairwise comparisons and computes
# the ranking scores computed using the algorithm above.

def pairwiseRank(P):
    y = np.size(P[:,0])
    N = np.ones(y)
    w = np.ones(y)
    for m in range(y-1):
        N = np.vstack((N,np.ones(y)))
    for u in range(y):
        for t in range(y):
            N[u,t] = P[u,t]+P[t,u]
    for i in range(y):
        w[i] = np.sum(P[i,:],axis=0)
    return w
    
    


exE = np.array([[0,1,0,1],[5,0,1,6],[8,8,0,5],[7,3,1,0]])

print(pairwiseRank(exE))