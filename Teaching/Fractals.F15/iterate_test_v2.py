
# an example program to iterate a function and make a time series plot
# David Feldman
# January 7, 2013

# IMPORT MODULES
from pylab import *
# this imports everything from pylab, aka matplotlib


# INITIALZE A BUNCH OF STUFF
n = 20 # number of iterates
time_series_list = [] # this will hold the time series.  initially it is empty

x = 40 # the initial condition

time_series_list.append(x) # add the initial condition to the list

n_list = range(0, n+1, 1) # the list of time values (0, 1, 2, ... n)


# ITERATE THE FUNCTION 
for i in range(n):
    x = (0.5)*x - 8 # <-- change this to iterate different functions5r
    time_series_list.append(x) # append each result to the time_series_list

    
# MAKE THE PLOT:  the basic command is plot(x,y), where x and y are both
# lists.  the two lists need to have the same number of elements
plot(n_list,time_series_list,color="blue", linewidth=2)
# (note: the color and linewidth options are optional)
# label the axes
xlabel("time t")
ylabel("x_t")

# set the y-limits so it looks nice
#ylim(0,1) uncomment and change this if you want to set the y-limits by hand

# display the plot
show()


