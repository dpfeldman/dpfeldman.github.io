
# an example program to iterate a function and make a time series plot
# for two different initial conditions
# David Feldman
# January 8, 2013

# IMPORT MODULES
from pylab import *
# this imports everything from pylab, aka matplotlib


# INITIALZE A BUNCH OF STUFF
n = 20 # number of iterates
X = [] # this will hold the time series.  initially it is empty
Y = [] # this will hold anther time series.  initially it is empty
# in this version I used capital letters for the lists

x = 40 # the initial condition
y = 20 # the other initial condition

X.append(x) # add the initial conditions to the list
Y.append(y) 

T = range(0, n+1, 1) # the list of time values (0, 1, 2, ... n)


# ITERATE THE FUNCTION 
for i in range(n):
    x = (0.5)*x - 8 # <-- change this to iterate different functions5r
    X.append(x) # append each result to the time_series_list
    y = (0.5)*y - 8
    Y.append(y)

    
# MAKE THE PLOT:  the basic command is plot(x,y), where x and y are both
# lists.  the two lists need to have the same number of elements
#plot(T,X,T,Y,color="blue", linewidth=2)
plot(T,X,"o",color="blue",label="foo")

plot(T,Y,"v",color="black", label="bar")
legend()

# label the axes
xlabel("time t")
ylabel("x_t, y_t")

# set the y-limits so it looks nice
#ylim(0,1) uncomment and change this if you want to set the y-limits by hand

# display the plot
show()


