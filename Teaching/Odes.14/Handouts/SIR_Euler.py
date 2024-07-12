# coding up Euler's method for the SIR model
# Differential Equations
# Sept 27, 2014
#
# This program uses Euler's method to solve the SIR model.
# More generally, it can solve DiffEQs of the form
#     dX/dt = f(X)
# where X is a vector.  Mathematically it's a vector, X will
# be a numpy array.

from numpy import *
import matplotlib.pyplot as plt

# Stuff to change **************
beta = 0.01 #note: beta = b/N
gamma = 3.0
TotalPopulation = 1000
InitialInfected = 10
DeltaT = 0.01
EndTime = 10 #how far to run for
# ******************************

def f(X):
    S = X[0]
    I = X[1]
    R = X[2]
    return( array([-beta*S*I, beta*S*I - gamma*I, gamma*I]) )

NumPoints = int(EndTime/DeltaT)
T = linspace(0,EndTime,NumPoints)

# Set initial conditions
R0 = 0
I0 = InitialInfected
S0 = TotalPopulation - InitialInfected

X = array([S0, I0, R0])
Spoints = [] #lists of S, I, and R values
Ipoints = []
Rpoints = []

print("R_0 = ", beta*TotalPopulation/gamma)

# Main Euler loop
for t in T:
    Spoints.append(X[0])
    Ipoints.append(X[1])
    Rpoints.append(X[2])
    #print(X)
    X = X + DeltaT*f(X)

# Plot the results!
plt.figure(1)
plt.plot(T,Spoints,label="Susceptible")
plt.plot(T,Ipoints,label="Infected")
plt.plot(T,Rpoints,label="Removed")
plt.ylabel("Number of People")
plt.xlabel("Time t")
plt.savefig("plot_SIR_temp.png") 
plt.legend(loc=7)
plt.show()
