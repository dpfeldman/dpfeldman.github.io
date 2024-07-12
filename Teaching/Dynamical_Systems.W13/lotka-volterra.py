# Program that uses Euler's method to numerically solve
# a system of coupled an ODEs
#
# This version is for the Lotka-Volterra model, but it can
# easily be modified to apply to other systems
#
# David Feldman
# January 13, 2013

from math import sin
from numpy import arange, empty
from pylab import plot,xlabel,ylabel,show,legend,figure

# This will solve coupled ODE's of the form
#     x' = Fx(x,y,t)
#     y" = Fy(x,y,t)

# **************************************
def Fx(x,y,t):
    return  (sin(t/5)*x)  - (0.5*x*y)

def Fy(x,y,t):
    return (0.2*x*y) - (0.6*y)

x_0 = 8.0 #initial x value
y_0 = 8.0 #initial y value
a = 0.0 # starting t value
b = 200.0 # ending t value
n = 10000 # number of steps
# **************************************

delta_t = (b-a)/n # stepsize for Euler
tpoints = arange(a,b,delta_t) #tpoints is an array
xpoints = [] # xpoints is a list
ypoints = [] # ypoints is a list

x = x_0
y = y_0
for t in tpoints:
    ypoints.append(y)
    xpoints.append(x)
    y = y + delta_t*Fy(x,y,t)
    x = x + delta_t*Fx(x,y,t)

# plot x and y vs t
figure(1)
plot(tpoints,ypoints,label="Foxes")
plot(tpoints,xpoints,label="Rabbits")
xlabel("Time t")
legend()

# plot x vs y
figure(2)
plot(xpoints, ypoints)
xlabel("x(t): Rabbits")
ylabel("y(t): Foxes")
show()

