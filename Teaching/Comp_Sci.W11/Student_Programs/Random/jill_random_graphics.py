#Jill Lee
#Sunday Jan 30, 2011
#The Automatic Ad Generator generates ads automatically using the name and slogan submitted by the user and randomly mixed colors.
#This code depends on John Zelle's graphics.py.

from graphics import *
from random import randrange

#Window 1: User inputs
win = GraphWin('Automatic Ad Generator',500,200)

#This is the direction for the user to enter a name and slogan.
intro=Text(Point(250,25),"Enter a name and slogan you'd like in your ad.\nClick the window when ready.")
intro.setFace('courier')
intro.setSize(10)

#Leading to the name field
query_name=Text(Point(158,100),"Name:")
query_name.setFace('courier')
query_name.setSize(10)

#Name field proper
input_name=Entry(Point(278,100),20)
input_name.setText('BP')
input_name.setFace('courier')
input_name.setSize(10)

#Leading to slogan field
query_slogan=Text(Point(165,125),"Slogan:")
query_slogan.setFace('courier')
query_slogan.setSize(10)

#Slogan field proper
input_slogan=Entry(Point(278,125),20)
input_slogan.setText('Beyond Prosecution')
input_slogan.setFace('courier')
input_slogan.setSize(10)

#Draw draw draw
intro.draw(win)
query_name.draw(win)
input_name.draw(win)
query_slogan.draw(win)
input_slogan.draw(win)

#Click when you're done
win.getMouse()

#Window 2: The output
win2 = GraphWin('Automatic Ad Generator',300,150)
win2.setCoords(0.0,0.0,3.0,1.5)

#Generating random colors. Four colors are needed.
r1=randrange(80,222)
g1=randrange(80,222)
b1=randrange(80,222)

r2=randrange(80,222)
g2=randrange(80,222)
b2=randrange(80,222)

r3=randrange(80,222)
g3=randrange(80,222)
b3=randrange(80,222)

r4=randrange(80,222)
g4=randrange(80,222)
b4=randrange(80,222)

#Draw the rectangles
strip1=Rectangle(Point(0.0,1.5),Point(3.0,0.95))
strip2=Rectangle(Point(0.0,0.95),Point(3.0,0.73))
strip3=Rectangle(Point(0.0,0.73),Point(3.0,0.53))
strip4=Rectangle(Point(0.0,0.53),Point(3.0,0.0))
#Then color them in
strip1.setFill(color_rgb(r1,g1,b1))
strip2.setFill(color_rgb(r2,g2,b2))
strip3.setFill(color_rgb(r3,g3,b3))
strip4.setFill(color_rgb(r4,g4,b4))
#Then color the outlines so they blend in
strip1.setOutline(color_rgb(r1,g1,b1))
strip2.setOutline(color_rgb(r2,g2,b2))
strip3.setOutline(color_rgb(r3,g3,b3))
strip4.setOutline(color_rgb(r4,g4,b4))
#Draw draw draw
strip1.draw(win2)
strip2.draw(win2)
strip3.draw(win2)
strip4.draw(win2)

#Get the name and the slogan from the input window
name=Text(Point(1.5,0.85),input_name.getText())
name.setFace('helvetica')
name.setSize(12)
name.setTextColor('white')
name.setStyle('bold')

slogan=Text(Point(1.5,0.64),input_slogan.getText())
slogan.setFace('helvetica')
slogan.setSize(12)
slogan.setTextColor('white')

#Draw draw
name.draw(win2)
slogan.draw(win2)

#So that the output doesn't just flash by
win2.getMouse()
win2.close()

