# File: naniel_hw4_randpicture.py
# Nathaniel Hilliard
# January 25, 2011

# This program uses the graphics and random import functions to make an 
# interesting picture. It also has a GUI where the user enters the desired
# number of circles to draw.

# More Comments?
# Make sure to clean up the format, place like statements together before you're done

from graphics import *
from random import randrange
from random import random
from time import sleep

# WINDOW #1: Interesting Picture
window = GraphWin("interesting picture", 300, 300)
window.setCoords(0.0, 0.0, 1.0, 1.0)
window.setBackground('dark goldenrod')

# Pre-drawn Circles
# Series of circles beginning from upper left
p1 = Point(0.1, 0.9)
c1 = Circle(p1, .1)
c1.setFill('black')
p2 = Point(0.19, 0.82)
c2 = Circle(p2, .085)
c2.setFill('purple')
p3 = Point(0.28, 0.75)
c3 = Circle(p3, 0.07)
c3.setFill('DarkOrchid3')
p4 = Point(0.37, 0.69)
c4 = Circle(p4, 0.055)
c4.setFill('blue')
p5 = Point(0.44, 0.65)
c5 = Circle(p5, 0.04)
c5.setFill('SteelBlue2')
p6 = Point(0.5, 0.63)
c6 = Circle(p6, 0.03)
c6.setFill('SteelBlue1')
p7 = Point(0.55, 0.625)
c7 = Circle(p7, 0.025)
c7.setFill('DarkSlateGray3')

# Series of circles beginning from lower right
p8 = Point(0.9, 0.1)
c8 = Circle(p8, 0.1)
c8.setFill('black')
p9 = Point(0.81, 0.17)
c9 = Circle(p9, 0.085)
c9.setFill('purple')
p10 = Point(0.72, 0.24)
c10 = Circle(p10, 0.07)
c10.setFill('DarkOrchid3')
p11 = Point(0.63, 0.3)
c11 = Circle(p11, 0.055)
c11.setFill('blue')
p12 = Point(0.56, 0.34)
c12 = Circle(p12, 0.04)
c12.setFill('SteelBlue2')
p13 = Point(0.5, 0.36)
c13 = Circle(p13, 0.03)
c13.setFill('SteelBlue1')
p14 = Point(0.45, 0.355)
c14 = Circle(p14, 0.02)
c14.setFill('DarkSlateGray3')

p1.draw(window)
c1.draw(window)
p2.draw(window)
c2.draw(window)
p3.draw(window)
c3.draw(window)
p4.draw(window)
c4.draw(window)
p5.draw(window)
c5.draw(window)
p6.draw(window)
c6.draw(window)
p7.draw(window)
c7.draw(window)
p8.draw(window)
c8.draw(window)
p9.draw(window)
c9.draw(window)
p10.draw(window)
c10.draw(window)
p11.draw(window)
c11.draw(window)
p12.draw(window)
c12.draw(window)
p13.draw(window)
c13.draw(window)
p14.draw(window)
c14.draw(window)

# WINDOW #2: GUI WINDOW
input_window = GraphWin("input window", 400, 200)
input_window.setBackground('light sea green')

t1 = Text(Point(115, 20), "How many more circles should I draw?: ")
t2 = Text(Point(180, 55), "(Recommendation: choose a number between 10 and 50): ")
t1.draw(input_window)
t2.draw(input_window)
query = Entry(Point(250 ,20), 5)
query.setText('0') 
query.draw(input_window)

t3 = Text(Point(180, 100), "Click On Screen When Ready")
t3.draw(input_window)

input_window.getMouse()

# User's Input
n = eval(query.getText()) 

for i in range(n):
      x = random() # x coordinate
      y = random() # y coordinate
      z = .06*random() # radius of circle

      p15 = Point(x, y)
      c15 = Circle(p15, z)

      r = randrange(180,255)
      g = randrange(60)
      b = randrange(100)

      c15.setFill(color_rgb(r, g, b))

      sleep(.3)

      p15.draw(window)
      c15.draw(window)


print("\n Click on the window to quit.")

input_window.getMouse()
input_window.close()

window.getMouse()
window.close()

