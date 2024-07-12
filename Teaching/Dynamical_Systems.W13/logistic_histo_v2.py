# this problem plots time series for the logistic equation
# and also makes histograms of the orbits
#
# David Feldman.  Feb 11 2013

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# CHOOSE AN R
#r = 3.1
#r = 3.835
r = 4.0
#r = 3.835 #period 3

# INITIAL CONDITIONS
x = 0.4
y = 0.41

# OPTIONS
IWantGrid = True

x_list = []
y_list = []
N=1000
nTransients = 10000
nPlot = 200

for i in range(nTransients):
    x = r*x*(1-x)
    y = r*y*(1-y)

for i in range(N):
    x = r*x*(1-x)
    y = r*y*(1-y)
    x_list.append(x)
    y_list.append(y)

#make a list for plotting time series
t=range(nPlot)
x_plot_list = []
y_plot_list = []
for i in t:
    x = r*x*(1-x)
    y = r*y*(1-y)
    x_plot_list.append(x)
    y_plot_list.append(y)

#plot Time Series
plt.figure(1)
plt.plot(t,x_plot_list,color="blue")

# the histogram of the data
plt.figure(2)
plt.hist(x_list, 8, normed=True, facecolor='blue', alpha=0.75)
plt.hist(y_list, 8, normed=True, facecolor='red', alpha=0.75)


# this version makes a line plot instead of bars
#plt.hist(x_list, 4, normed=True, color='blue', histtype='step')
#plt.hist(y_list, 100, normed=True, color='red', histtype='step')
# alpha controls the transparency


plt.xlabel('x')
plt.ylabel('Frequency')

#plt.axis([1, 0, 0, 1.3])
plt.grid(IWantGrid)

plt.show()
