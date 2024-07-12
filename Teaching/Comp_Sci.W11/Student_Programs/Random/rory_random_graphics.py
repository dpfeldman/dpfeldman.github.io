# Graphics Program: Random
# by Rory Ives
# Due January 30th, 2011
#
# Requests two numbers from the user, 
# using one to decide how many circles
# it will make and the other to determine
# the size of the circles.
# The placement and color of the circles
# are chosen randomly, along with the
# color of the background, which has
# a slight preference for being chartreuse.

from graphics import * 
from random import *
# These imports functions from other modules.

inwin = GraphWin("Gimme numbas!", 400, 200) # Creates the first window
inwin.setCoords(0.0, 0.0, 1.0, 1.0) # Makes coordinates relative
# Text ensues!
explanation = Text( Point(0.5, 0.90), "This program creates randomly colored\ncircles on a randomly colored background!")
circtxt = Text( Point(0.5, 0.75), "How many circles do you want?")
circnum = Entry( Point(0.5, 0.6), 10) # Input for the number of circles
bigtxt1 = Text( Point(0.5, 0.45), "How big do you want them to be?")
bigtxt2 = Text( Point(0.5, 0.37), "(For this, the smaller the number, the bigger the potential circle!)")
bigtxt2.setSize(10)
bignum = Entry( Point(0.5, 0.25), 10) # Input for the size of circles
clickme = Text( Point(0.5, 0.1), "Click when you've entered your choices!")
tnx = Text( Point(0.5, 0.1), "Thanks for using this! I hope it pleased you.")
# Then everything gets "drawn."
explanation.draw(inwin)
circtxt.draw(inwin)
circnum.draw(inwin)
bigtxt1.draw(inwin)
bigtxt2.draw(inwin)
bignum.draw(inwin)
clickme.draw(inwin)

inwin.getMouse() # Finalizes entries

clickme.undraw()
tnx.draw(inwin)
# Replaces "click me" text with a thank you message.

num = eval(circnum.getText())
size = eval(bignum.getText())
# Converts input numbers to functional terms

imwin = GraphWin("Your partially random design!", 350,350) # Creates the second window!
imwin.setCoords(0.0, 0.0, 1.0, 1.0) # Makes coordinates relative

r = randrange(227)
g = randrange(255)
b = randrange(50)
# Defines individual color variables

imwin.setBackground(color_rgb(r, g, b)) # Sets the background color with randomized variables

for stuff in range(num): 
    x = random()
    y = random()
    z = random()/size
    r = randrange(255)
    g = randrange(255)
    b = randrange(255)
    circ = Circle(Point(x, y), z)
    circ.setFill(color_rgb(r, g, b))
    circ.draw(imwin)
    #Creates a loop that will create the desired amount of circles in the desired size range


imwin.getMouse()
imwin.close()
# Closes the second window

inwin.getMouse()
inwin.close()
# Closes the first window

