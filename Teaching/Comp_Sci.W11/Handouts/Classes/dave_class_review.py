
# This little program reviews some
# things about classes and objects

from graphics import *

def main():

    # create instance of the Graph Win class
    win = GraphWin("",200,200) #<-- constructor

    # create instance of the circle class
    c = Circle(Point(100,100),40) #<-- constructor
    c.draw(win) #<-- method

    # create another instance of a circle
    c2 = Circle(Point(50,50), 25)
    c2.setFill("purple")
    c2.draw(win)

    p1 = c2.getP1() #<--accessor function
    # gets a point in the corner of the bounding box
    p1.draw(win) 

    win.getMouse()
    win.close()

main()
