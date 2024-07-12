# this program uses the scipy function odeint to generate solutions
# to the SIR model
#
# odeint is an implementation of a 4th-order Runge-Kutta algorithm
# with an adaptive stepsize.
#
# Differential Equations
# Sept 29, 2014
#
# This programcan solve DiffEQs of the form
#     dX/dt = f(X,t)
# where X is a vector.  note that the RHS of the diffEQ has to
# have a t in it.  

from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Stuff to change **************
beta = 0.01 #note: beta = b/N
gamma = 2.0
TotalPopulation = 1000
InitialInfected = 10
DeltaT = 0.01
EndTime = 10 #how far to run for
# ******************************
print("R_0 = ", beta*TotalPopulation/gamma)

# Define the function which is the RH side of the DiffEQ
def f(X,t):
    S = X[0]
    I = X[1]
    R = X[2]
    dS = -beta*S*I
    dI = beta*S*I - gamma*I
    dR = gamma*I
    return( [dS, dI, dR] )

T = arange(0,EndTime,DeltaT)
# note: DeltaT is *not* used by odeint.  We use it to fill up
# the array of time values.  But then odeint figures out what
# Delta T it needs to use to come up with a good solution to the
# Differential Equation
#
# note: you could also initial T using linspace
# T = linspace(0,EndTime,NumPoints)

# Set initial conditions:
R0 = 0
I0 = InitialInfected
S0 = TotalPopulation - InitialInfected
InitialCondition = [S0, I0, R0]

# Call odeint:
SIR_solution = odeint(f, InitialCondition, T)
# f must be a function of the vector X and time t
# InitialCondition is a vector of initial conditions
# T is an array of time values
# odeint will then solve the DiffEQ by figuring out the X
# values for each time value in the array T
# odeint returns a list of vectors; each vector corresponds
# to the value of X for that T.  I.e., it would return a
# list of the following form:
# [ [S0, I0, R0], [S1, I1, R1], [S2, I2, R2], ... ]
#

# We now need to extract S(t), I(t), and R(t) as their own
# lists so that we can plot them.
S = [vector[0] for vector in SIR_solution]
I = [i[1] for i in SIR_solution]
R = [i[2] for i in SIR_solution]
# Equivalently, one could write:
# S = SIR_solution[:, 0]
# I = SIR_solution[:, 1]
# R = SIR_solution[:, 2]


# Plot the results:
plt.figure(1)
plt.plot(T,S,label="Susceptible")
plt.plot(T,I,label="Infected")
plt.plot(T,R,label="Removed")
plt.ylabel("Number of People")
plt.xlabel("Time t")
plt.savefig("plot_SIR_temp.png") 
plt.legend(loc=7)
plt.show()
