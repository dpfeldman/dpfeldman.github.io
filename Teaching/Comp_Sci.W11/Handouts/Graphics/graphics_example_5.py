# Example Program for class, Thursday 20 Jan. 2011
# This program shows how to use the
# set coords feature of
#Zelle's GraphWin module 

from graphics import *

# download the module here at
# http://mcsp.wartburg.edu/zelle/python/

window = GraphWin("pixel coords", 100,100)
# create an instanceof the GraphWin class

# let's suppose we want to make a circle
# in the center of the window
p1 = Point(50,50)
c1 = Circle(p1,20)
p2 = Point(90,90)
c1.draw(window)
p2.draw(window)

# now suppose that later in the development
# process we want to make the window bigger
# but circle should stay in the center
# this would be a pain, since we would need
# to change lots of pixle positions

# here is an alternative method for specifying
# the positions of points that can be much
# simpler

# i'll illustrate this in a different window

win2 = GraphWin("simpler coords", 100,100)

win2.setCoords(0.0, 0.0, 1.0, 1.0)
# this makes a new set of coordinates
# that go from (0,0) in the lower left
# to (1,1) in the upper right

p3 = Point(0.5,0.5)
c3 = Circle(p3,0.2)
p4 = Point(0.9,0.1)
c3.draw(win2)
p4.draw(win2)

# note that the origin is now in
# the lower left of the window instead
# of the upper left


# close the windows when there is a mouse click
window.getMouse()
window.close()

win2.getMouse()
win2.close()
