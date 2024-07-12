# This program was written by Paul Smith on 28Jan2011

# It functions to prompt a user for a desired number of circles
# and their radius. These variables are then looped through
# an algorithm that assigns each circle a random color. The
# circle radius has also been randomized.

from graphics import *
from random import random
from random import randrange


win = GraphWin("Random Circle Generator", 400, 300)
win.setCoords(0.0, 0.0, 3.0, 4.0)

Title = Text(Point(1.5,3.5), "Random Circle Generator v1")
Title.setStyle("bold")
Title.draw(win)

Text(Point(1,3), "Number of circles:").draw(win)

input = Entry(Point(2,3) ,5)
input.setText("lots")
input.draw(win)

RectangleA = Rectangle(Point(1,1.5), Point(2,2.5))
RectangleA.setFill('purple')
RectangleA.draw(win)

button = Text(Point(1.5,2), "Enter # of Circles!")
button.setStyle("bold")
button.draw(win)

win.getMouse()

circNUM = eval(input.getText())

button.setText("Enter Size of Circles!")
button.setStyle("bold")

Text(Point(1,2.75), "Size of circles:").draw(win)

input = Entry(Point(2, 2.75) ,5)
input.setText("(0.01)-1")
input.draw(win)

win.getMouse()

circSIZE = eval(input.getText())

win.getMouse()

button.setText("Generate Circles!")
button.setStyle("bold")

win.close()

win2 = GraphWin("Random Circles", 300, 300)
win2.setCoords(0.0, 0.0, 1.0, 1.0)

for i in range (circNUM):

    r = randrange(0,100)
    g = randrange(256)
    b = randrange(256)
    x = random()
    y = random()
    randCIRC = Circle(Point(x, y) ,random()*circSIZE)
    randCIRC.setFill(color_rgb(r, g, b))
    randCIRC.draw(win2)


win2.getMouse()
win2.close()

