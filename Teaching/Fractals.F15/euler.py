# Program that uses Euler's method to numerically solve an ODE
#
# David Feldman
# January 13, 2013

from math import exp
from numpy import arange, empty
from pylab import plot,xlabel,ylabel,show,legend

# This will solve ODE's of the form y' = F(y,t)

# **************************************
def F(y,t):
    return -0.2*(y-20)

y_0 = 80
a = 0.0 # starting t value
b = 50.0 # ending t value
n = 100 # number of steps
# **************************************

delta_t = (b-a)/n # stepsize for Euler

tpoints = arange(a,b,delta_t) #tpoints is an array
ypoints = [] #ypoints is a list
exact_ypoints = [] 

y = y_0
for t in tpoints:
    ypoints.append(y)
    y = y + delta_t*F(y,t)

# for this ODE we can get an exact solution.
# let's plot it along with the Euler solution
# make the tpoints for the exact solution
dt = (b-a)/1000 
tpoints2 = arange(a, b, dt)
for t in tpoints2:
    exact_ypoints.append(20 + 60*exp(-0.2*t))    


plot(tpoints,ypoints,label="Euler")
plot(tpoints2,exact_ypoints,label="Exact") #plot exact solution
xlabel("t")
ylabel("y(t)")
legend()
show()

