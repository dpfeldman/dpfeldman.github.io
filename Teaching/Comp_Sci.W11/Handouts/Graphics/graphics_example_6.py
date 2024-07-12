# Example Program for class, Thursday 20 Jan. 2011
# This program shows a different way to set
# colors, and also how to use a random number
# generator to make random colors

from graphics import *

# download the module here at
# http://mcsp.wartburg.edu/zelle/python/

# import the randrange function
# from the random module
from random import randrange

window = GraphWin("random color window", 400,200)
# create an instanceof the GraphWin class

# set r, g, b equal to random integers
# between 0 and 255
r = randrange(256)
g = randrange(256)
b = randrange(256)

# make a window with the random color as
# the background
window.setBackground(color_rgb(r, g, b))

#print the random colors
print("The color of the window is:")
print("\tRed =",r)
print("\tGreen =",g)
print("\tBlue =",b)

print("\nClick on the window to quit.")


# close the windows when there is a mouse click
window.getMouse()
window.close()

