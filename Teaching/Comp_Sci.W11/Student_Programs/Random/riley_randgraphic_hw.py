#riley_randgraphic_hw.py
#Riley Thompson
#1/31/11
#A Program that generates a random pattern of circles based on
# user-inputted information (number & size)

from graphics import *
from random import randrange
from time import sleep

def circles(win, s):
    c1 = randrange(11)
    c2 = randrange(11)
    r = randrange(200)
    g = randrange(200)
    b = randrange(200, 256)
    circle = Circle(Point(c1, c2), s)
    circle.setFill(color_rgb(r, g, b))
    circle.draw(win)
    
def main():

    #draw windows
    win = GraphWin("Picture", 450, 450)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    win2 = GraphWin("Options", 400, 250)
    win2.setCoords(0.0, 0.0, 10.0, 10.0)
    win2.setBackground(color_rgb(32, 61, 255))
    back = Rectangle(Point(.5, .5), Point(9.7, 9.3))
    back.setFill(color_rgb(136, 152, 255))
    back.setOutline(color_rgb(136, 152, 255))
    back.draw(win2)

    # in win2:
    # Title question
    title = Text(Point(3.7, 8), 'Number of circles:')
    title.setSize(20)
    title.setStyle('bold')
    title.draw(win2)

    title2 = Text(Point(5, 5), 'Enter a size between 1 and 5:')
    title2.setSize(20)
    title2.setStyle('bold')
    title2.draw(win2)

    # Entry box for number of circles
    box1 = Entry(Point(3, 6.5), 8)
    box1.setSize(20)
    box1.setStyle('bold')
    box1.draw(win2)

    box2 = Entry(Point(3, 3.5), 8)
    box2.setSize(20)
    box2.setStyle('bold')
    box2.draw(win2)

                 
    #ready "button"
    t = Text(Point(5, 1.6), "Click to draw")
    t.setSize(22)
    t.setStyle('bold')
    t.draw(win2)

    # wait for mouse
    win2.getMouse()

    #number & size
    n = eval(box1.getText())
    s = eval(box2.getText())

    for i in range (n):
        circles(win, s)
        sleep(.1)

    t.setText('Click Both Windows When Finished')
    win2.getMouse()
    win2.close()
    win.getMouse()
    win.close()
    
    
main()

