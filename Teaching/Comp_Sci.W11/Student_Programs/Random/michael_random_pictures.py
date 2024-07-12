#Michael Jenks
#January 30, 2011
#Random Picture imaging

from graphics import*
from random import*
from time import sleep
#I decided to start off with two windows
winpic=GraphWin("Picture Window",800,800)
win=GraphWin("Input Window")

win.setBackground(color_rgb(200,30,56))

text1=Text(Point(50,20),"Enter Number")
text1.draw(win)
text2=Text(Point(100,80),"Do not use program if")
text2.draw(win)
text3=Text(Point(100,100),"you experience epilepsy")
text3.draw(win)
text4=Text(Point(100,50),"WARNING")
text4.draw(win)
box=Entry(Point(150,20),5)
box.setText("2000")
box.draw(win)
win.getMouse()

for i in range(800):
    slash=Circle(Point(i,i),10)
    slash.setFill(color_rgb(i,i,i))
    slash.draw(winpic)
#This Makes a really cool slash across the screen

for i in range(eval(box.getText())):
    x=randrange(800)
    y=randrange(800)
    z=randrange(800)
    circ=Circle(Point(x,y),z)
    bubble=Text(Point(x,y),"Crazy Bubbles")
    r=randrange(256)
    g=randrange(256)
    b=randrange(256)
    bubble.setTextColor(color_rgb(r,g,b))
    bubble.draw(winpic)
    circ.setOutline(color_rgb(r,g,b))
    circ.draw(winpic)
    winpic.setBackground(color_rgb(r,g,b))
   

                         
#try 2000 in the range it would make for an awesome screen saver

