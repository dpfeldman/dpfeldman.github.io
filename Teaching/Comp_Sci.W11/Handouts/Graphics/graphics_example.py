# Example Program for class, Monday 17 Jan. 2011
# This program shows some of the basics of the
# GraphWin module and is an introduction to objects

#import graphics

from graphics import *

#load the graphics module
# this will only work if you have the graphics.py module downloaded
# and in a directory where python can find it
# download the module here at
# http://mcsp.wartburg.edu/zelle/python/

window = GraphWin("example window") # create an instance of the GraphWin class

p1 = Point(10,50) # create an instance of the Point class
# p1 is the name of the particular point
p2 = Point(25,25) # another point

p1.draw(window)
#p2.draw(window)

# the window is 200 x 200.  0, 0, is in the upper left
p3 = Point(190,190)
#p3.draw(window)

#print(p1.getX())

# examples with circles



c = Point(100,100)
circ = Circle(c, 30)
circ.setFill('purple')
circ.draw(window)

circ2 = Circle( Point(200,200), 60 )
circ2.setFill('blue')
circ2.draw(window)

# example with lines
cat = Line(Point(20,100), Point(180,100))
cat.draw(window)
