# Example Program for class, Monday 19 Jan. 2011
# This program shows more of the basics of Zelle's
# GraphWin module 

#import graphics

from graphics import *

#load the graphics module
# this will only work if you have the
# graphics.py module downloaded and
# in a directory where python can find it
# download the module here at
# http://mcsp.wartburg.edu/zelle/python/

window = GraphWin("example window", 400,100) # create an instance 
# of the GraphWin class

window.setBackground('green4')

p1 = Point(10,50)  # create an instance of the Point class
p2 = Point(25,25)  # another point
p1.draw(window)
p2.draw(window)


c = Point(100,100)
circ = Circle(c, 30)
circ.setFill('purple')
circ.draw(window)

circ2 = Circle( Point(150,80), 25 )
circ2.setFill('purple2')
circ2.draw(window)

circ3 = Circle( Point(200,70), 20 )
circ3.setFill('purple3')
circ3.draw(window)

circ4 = Circle( Point(250,40), 10 )
circ4.setFill('purple4')
circ4.draw(window)
# example with lines

cat = Line(Point(60,40), Point(100,40))
cat.draw(window)

greeting = Text( Point(320,70), 'i like purple circles')
greeting.draw(window)

shape = Polygon( Point(40,20), Point(40,40), Point(50,60), Point(25,55))
shape.setFill('pink')
shape.setWidth(4)
shape.setOutline(color_rgb(234,0,0))
shape.draw(window)

# close the window if there is a mouse click
# we'll talk more about this on thursday
# but if the non-closing window is really bugging
# you, try this:

window.getMouse()
window.close()
