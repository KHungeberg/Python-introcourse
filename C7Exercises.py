# CHAPTER 7 EXERCISES

# INTRO 

# Working with plots: 

# When working with plots we want to use the module matplotlib.plotly 
import numpy as np
import matplotlib.pyplot as plt 
import math as ma
import random as rd
import pandas as pd
# if we have a list or tuple of x and y values we could make a plot as such: 

# plt.plot(x,y) Plots the values 
# plt.title("string") gives a title to the plot 
# plt.xlabel("string") title to the x-axis 
# plt.ylabel("string") title to the y-axis 
# plt.xlim([a,b]) puts x within a closed interval 
# plt.ylim([c,d]) puts y withing a closed interval 
# plt.show() prints the plot in the "plots" window.

# here are some of the options within the plot command: 
    
# plt.plot(x,y,c="color",label="title",linestyle="linestyle",marker='mark',markerfacecolor="color",
# markersize = number)

# help(plt.plot) #This shows everything we want to know about plt.plot. 

# EXERCISE 7A

# Replicate the given plot: 
 #UNCOMMET LINE 31-44 FOR THIS EXERCISE
# x = [-3,-1,0,3,3]

# y = [0,-2,0,-1,2]

# plt.plot(x,y,c="red")
# plt.plot(x,y,"b*")
# plt.title("Sketch of Cassiopeia star constalation")
# plt.xlabel("Relative x value from center star")
# plt.ylabel("Relative y value from center star")
# plt.grid()
# plt.ylim([-3,3])
# plt.xlim([-4,4])
# plt.show()

# EXERCISE 7B

# Create two different vectors, x and y, each containing 2000 random numbers, uniformly distributed between -10
# and 10.
# Make a scatterplot of the points x,y where the absolute value of x or y is over 5 and the vectornorm of (x,y) is 
# smaller than 10 

# To create the random vectors well use our random vector function from an earlier assignment
# UNCOMMENT LINE 55-74 FOR THIS PLOT. 
# def randomSequence(mu,R,N):
#         Q = R*(np.random.rand(N))+mu-R/2
#         return Q


# xvals = randomSequence(0, 20, 2000)
# yvals = randomSequence(0, 20, 2000)

# for i in range(2000):
#     if not(ma.sqrt(xvals[i]**2+yvals[i]**2)<10 and max(abs(xvals[i]),abs(yvals[i]))>5):
#         xvals[i] = 3000
#         yvals[i] = 3000

# filterx = xvals[xvals!=3000]
# filtery = yvals[yvals != 3000]

# plt.plot(filterx,filtery,".")
# plt.xlim([-10,10])
# plt.ylim([-10,10])
# plt.show()

# EXERCISE 7C

# To make a histogram we use plt.hist(x,number of bins). where x is a list of observations. 

# 1 ) Simulate sequences of fair coin tosses and plot histograms for N = 10, N = 100 and N = 1000. Remember
# to set title and labels for your histogram appropriately.

# From which of the histograms can you best see that PH = PT = 1/2

# Uncomment line 88-92 for this part of the exercise. 

# x = np.random.rand(1000)<0.5
# x = x.astype(int)

# plt.hist(x,bins=2,color="blue",ec="black")
# plt.show()
    
# Answer ofcourse it is with N=1000

# How would you change the code to generate a sequence of tosses with an unfair coin, where PH = 0.7
# and PT = 0.3?:

# Answer: i could write x = np.random.rand(10)<(0.3 or 0.7). 

# Write a script that simulates a sequence of N throws of a fair six-sided die and plots the distribution of
# the outcomes in a histogram with 6 bins. Run your code for N = 10, N = 100 and N = 1000 throws.

# Uncomment line 105-111 for this part of the exercise. 
# q = np.ones(100)

# for i in range(100):
#     q[i] = rd.randint(1,6)
    
# plt.hist(q,6,ec="black")
# plt.show()

# How large must N be to show that the probability of each outcome is identical? 

# Answer: at N=1000 it is very clear 

# Compared to the coin-toss example, why do we in general need a longer sequence of dice throws to
# approximate the underlying probability distribution in the histogram?

# Because the chance that we get P(X != x) = 5/6 here. So the chance for "error" is much bigger than in the coin example. 

# EXERCISE 7D

# Create a plot that shows the exponential decay of carbon 14 in organic material. The plot must show the age
# of the organic material on the y-axis and the corresponding percentage of remaining carbon 14 on the x-axis
# (such that N0 = 100 and 0 <= N <= 100). Use a lineplot to illustrate this by creating a list of x-values and a list
# of the corresponding y-values. The more points you use, the smoother the curve will look. With 1000 points,
# you will get a plot as shown in the following figure. Give your plot a meaningful title and labels for the axis.

# We'll use our random vector generator to create the values of N. 

# def randomSequence(mu,R,N):
#         Q = R*(np.random.rand(N))+mu-R/2
#         return Q

# N = np.sort(randomSequence(50, 100, 1000))

# lmda = ma.log(2)/5700

# t = -((1/lmda)*np.log(N/100))

# plt.plot(N,t,marker='.')
# plt.show()

# A tusk of a woolly mammoth discovered in Siberia is analysed. The ratio between carbon 12 and 14 is
# found to only be one tenth of the ratio measured from ivory of recently deceased (present day) elephants.
# Look at your plot to verify that the mammoth is around 19,000 years old.

# Answer: To test this we could use plt.ylim([18000,20000]) and see that we are around 10% on the x axis. 

# Carbon 14 measurements are considered unreliable for estimating organic material older than 50,000 years.
# Look at your plot and consider why this is so.

# Answer: You can see that a miniscule change in organich material would mean a huge difference in the estimated age. A small 
# percent interval in estimated organic material would mean a huge estimated age interval. 

# EXERCISE 7E

# Make a line graph with the year on the x-axis and the yearly mean temperature on the y-axis. Set the range of
# the x-axis to begin at 1920 and end at 2010. Your plot should look like the one in the following figure. Make
# sure to set appropriate labels and title.

weather = pd.read_csv("UKTemperature.csv")

vecweather = np.array(weather)

monthavg = np.ones(101)

for i in range(101):
    monthavg[i] = np.mean(vecweather[i,1:13],axis=0)

years = vecweather[:,0]

avg = vecweather[:,13]

plt.plot(years,avg,label="Annual mean")
plt.plot(years,monthavg,label="monthly mean",c="red")
plt.title("Weather in UK (1912-2012)")
plt.xlabel("Year")
plt.ylabel("Yearly average in celcis")
plt.xlim([1920,2010])
plt.ylim([7,10.5])
plt.legend(loc="upper left")
plt.savefig(fname="weatherfig")
plt.show()
