# alonso_homework3.py
# "Click for Circles" Program
# This program generates circles based
# on mouse clicks.

from graphics import *
from random import randrange

def main():

    win = GraphWin("Alonso's Homework", 400,400)
    win.setBackground('white')
    win.setCoords(0,0,10,10)

    words = Text(Point(5,5), "Please Click on 10 Different Places")
    words.setFace('helvetica')
    words.setSize(15)
    words.setStyle('bold')
    words.setTextColor('cyan4')
    words.draw(win)

    for i in range(10):

        p1 = win.getMouse()
        a = p1.getX()
        a = int(a)
        b = p1.getY()
        c = a * (1/2)

        r = randrange(256)
        g = randrange(256)
        b = randrange(256)

        circ = Circle(p1,c)
        circ.setFill(color_rgb(r,g,b))
        circ.draw(win)

    words2 = words.clone()
    words2.setText("Thank You For Clicking")
    words2.setTextColor('yellow')

    words.undraw()
    words2.draw(win)
    
    win.getMouse()
    words2.undraw()
    
    win.getMouse()
    win.close()

main()

    
