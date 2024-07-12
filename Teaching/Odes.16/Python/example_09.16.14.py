# Examples from class.  9/16/14
# Differential Equations
# Dave Feldman.  College of the Atlantic

from math import *

# Two ways to print out the log of 1, 2, ...., 11.
for i in range(1,11):
    print(log(i))

for i in range(10):
    print(log(i+1))

# Variables can be strings (words)
x = "hello"
print(x)

# Python has lists built in
X = [ 7, 55, 88.4, "cheese"]

# **********************************************************************
# Two ways to make lists
Z = [] # Z is an empty list
for i in range(10):
    Z.append(sin(i))

# List comprehension
Z2 = [sin(i) for i in range(10)]
# Z and Z2 are the same
# **********************************************************************

# Let's learn about if statements
x = 20
if(x>10):
    print("x is big")
    print("x is seriously big")

if(x<10):
    print("x is small")

if(x==20):
    print("x is twenty!")

# note that if(x=20) does not work!










