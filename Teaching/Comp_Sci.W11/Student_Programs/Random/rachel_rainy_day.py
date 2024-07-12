#Rachel Guttmacher
#Homework 4: Write a program that uses Zelle's graphics package and some
#random number features to make an interesting or asthetically applealing
#picture using random shapes and colors.

from graphics import *
from random import *
from time import sleep

win1 = GraphWin("A Rainy Day",500,500)
win1.setCoords(0.0,0.0,1.0,1.0)
win1.setBackground(color_rgb(206,215,255))

ground = Rectangle(Point(0,.1),Point(1,0))
ground.setFill(color_rgb(30,120,40))
ground.draw(win1)

house = Polygon(Point(.1,.1),Point(.1,.2),Point(.2,.2),Point(.2,.1))
house.setFill(color_rgb(255,102,0))
house.draw(win1)

roof = Polygon(Point(.05,.2),Point(.15,.3),Point(.25,.2))
roof.setFill(color_rgb(153,102,51))
roof.draw(win1)

door = Rectangle(Point(.14,.15),Point(.16,.1))
door.setFill(color_rgb(153,102,51))
door.draw(win1)

head = Circle(Point(.6,.17),.01)
head.setFill(color_rgb(255,209,162))
head.draw(win1)

body = Rectangle(Point(.59,.15),Point(.61,.1))
body.setFill(color_rgb(255,209,162))
body.draw(win1)

win2 = GraphWin("Weather Prediction?",300,300)
win2.setCoords(0.0,0.0,1.0,1.0)

t1 = Text(Point(.5,.8), "How much will it rain today?")
t1.draw(win2)

t2 = Text(Point(.5,.7), "Enter # of drops (0=none, 500=downpour):")
t2.setSize(10)
t2.draw(win2)

query = Entry(Point(.5,.6),8)
query.setText("250")
query.draw(win2)

t3 = Text(Point(.5,.4), "Click HERE to make your")
t3.setSize(15)
t3.draw(win2)

t4 = Text(Point(.5,.3), "prediction come true!")
t4.setSize(15)
t4.draw(win2)

win2.getMouse()

prediction = eval(query.getText())

t7 = Text(Point(.5,.05),"Click HERE to close.")

def draw_rain():
    x = random()
    y = random()
    rain = Line(Point(x,y),Point(x,y-.02))
    rain.setOutline(color_rgb(0,0,204))
    rain.draw(win1)
    
if prediction == 0:
    win2.close()
    t5 = Text(Point(.5,.7), "What beautiful weather!")
    t5.setSize(20)
    t5.draw(win1)
    sun = Circle(Point(0,1),.1)
    sun.setFill(color_rgb(255,255,0))
    sun.draw(win1)
    
if prediction > 0:
    win2.close()
    handle = Line(Point(.585,.125),Point(.585,.19))
    handle.draw(win1)
    umbrella = Polygon(Point(.555,.19),Point(.585,.22),Point(.615,.19))
    r = randrange(255)
    g = randrange(255)
    b = randrange(255)
    umbrella.setFill(color_rgb(r,g,b))
    umbrella.draw(win1)
    t6 = Text(Point(.5,.5), "Glad you had that umbrella!")
    t6.setSize(20)
    t6.draw(win1)
    for i in range(prediction):
        draw_rain()
        sleep(.025)

t7.draw(win1)

win1.getMouse()
win1.close()

