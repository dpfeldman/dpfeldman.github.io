#Dale Quinby
#Comp Sci HW 4
# 1/26/11
#
#Random circles: colors, size, and quantity of your choice, so as to learn
# how to use random funtions, graphics windows, etc.
#Just remembered that exponents are **, not ^.
#This may help future improvements.

from graphics import *

from random import *

from time import *


draw_window = GraphWin("draw_window", 600, 600)
draw_window.setCoords(0.0, 0.0, 1.0, 1.0)

text_window = GraphWin("text_window", 500, 500)
text_window.setCoords(0.0, 0.0, 1.0, 1.0)

ask_r1 = Text(Point(0.5, 0.9), "Lower red range limit: ")
ask_g1 = Text(Point(0.5, 0.7), "Lower green range limit: ")
ask_b1 = Text(Point(0.5, 0.5), "Lower blue range limit: ")

ask_r2 = Text(Point(0.5, 0.8), "Upper red range limit: ")
ask_g2 = Text(Point(0.5, 0.6), "Upper green range limit: ")
ask_b2 = Text(Point(0.5, 0.4), "Upper blue range limit: ")

ask_r1.draw(text_window)
ask_g1.draw(text_window)
ask_b1.draw(text_window)

ask_r2.draw(text_window)
ask_g2.draw(text_window)
ask_b2.draw(text_window)

query_r1 = Entry(Point(0.9, 0.9), 5)
query_g1 = Entry(Point(0.9, 0.7), 5)
query_b1 = Entry(Point(0.9, 0.5), 5)

query_r2 = Entry(Point(0.9, 0.8), 5)
query_g2 = Entry(Point(0.9, 0.6), 5)
query_b2 = Entry(Point(0.9, 0.4), 5)


query_r1.draw(text_window)
query_g1.draw(text_window)
query_b1.draw(text_window)

query_r2.draw(text_window)
query_g2.draw(text_window)
query_b2.draw(text_window)


# Need to figure out a better way of doing size.
#ask_z1 = Text(Point(0.5, 0.3), "Fraction of window size of smallest circle \n in 1/n format:") 
#ask_z1.draw(text_window)
#ask_z2 = Text(Point(0.5, 0.2), "Fraction of window size of biggest circle \n in 1/n format:")
#ask_z2.draw(text_window)
#query_z1 = Entry(Point(0.9, 0.3), 5)
#query_z1.draw(text_window)
#query_z2 = Entry(Point(0.9, 0.2), 5)
#query_z2.draw(text_window)
ask_z = Text(Point(0.5, 0.3), "What fraction of the window size would you \n like the circles?")
query_z = Entry(Point(0.9, 0.3), 5)
ask_z.draw(text_window)
query_z.draw(text_window)

ask_number = Text(Point(0.5, 0.2), "How many circles would you like?")
ask_number.draw(text_window)
query_number = Entry(Point(0.9, 0.2), 5)
query_number.draw(text_window)

start = Text(Point(0.5, 0.1), "To begin, please click this box.")
start.draw(text_window)

text_window.getMouse()

r_range1 = eval(query_r1.getText())
r_range2 = eval(query_r2.getText())
g_range1 = eval(query_g1.getText())
g_range2 = eval(query_g2.getText())
b_range1 = eval(query_b1.getText())
b_range2 = eval(query_b2.getText())
#z_range1 = eval(query_z1.getText())
#z_range2 = eval(query_z2.getText())

number = eval(query_number.getText())
               
for i in range(number):
    x = random()
    y = random()
   # z = randrange(z_range1**-1, z_range2**-1)
    z = eval(query_z.getText())
    #z = random()

    r = randrange(r_range1, r_range2)
    g = randrange(g_range1, g_range2)
    b = randrange(b_range1, b_range2)

    circ = Circle(Point(x, y), z)
    circ.draw(draw_window)
    circ.setFill(color_rgb(r, g, b))

    sleep(0.1)

text_window.close()

text2_window = GraphWin("text2_window", 400, 400)
text2_window.setCoords(0,0,1,1)

close = Text(Point(0.5, 0.5), "To close, please click this box, then the picture.")
close.draw(text2_window)

text2_window.getMouse()
text2_window.close()
draw_window.getMouse()
draw_window.close()

