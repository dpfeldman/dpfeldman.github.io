#Rebecca Coombs
# graphics homework 3
# Jan 23

#Rebecca Coombs
# Jan 23 Homework
# This draws a picture of a mountain scene using graphics
# uses randrange function to make random colors of the flowers



from graphics import *


window = GraphWin("Pretty Scenery",500,500)
window.setCoords(0.0, 0.0, 1.0, 1.0)


#sky color
window.setBackground(color_rgb(135,206,250))



grass = Rectangle(Point(0.0,0.0),Point(1.1,0.2))
grass.setFill(color_rgb(85,107,47))
grass.setOutline(color_rgb(85,107,47))
grass.draw(window)



#sun
sun = Circle(Point(0.2,0.8),.05)
sun.setFill(color_rgb(238,221,130))
sun.draw(window)

ray = Line(Point(0.26,0.8),Point(0.33,0.8))
ray.setFill(color_rgb(238,221,130))
ray.draw(window)

ray2 = Line(Point(0.07,0.8),Point(0.14,0.8))
ray2.setFill(color_rgb(238,221,130))
ray2.draw(window)

ray3 = Line(Point(0.2,0.86),Point(0.2,0.93))
ray3.setFill(color_rgb(238,221,130))
ray3.draw(window)

ray4 = Line(Point(0.2,0.74),Point(0.2,0.67))
ray4.setFill(color_rgb(238,221,130))
ray4.draw(window)


#mountains
mtn3 = Polygon(Point(0.3,0.2),Point(0.45,0.43),Point(0.65,0.2))
mtn3.setFill(color_rgb(205,133,63))
mtn3.setOutline(color_rgb(205,133,63))
mtn3.draw(window)

mtn = Polygon(Point(0.0,0.2),Point(0.2,0.5),Point(0.5,0.2))
mtn.setFill(color_rgb(205,133,63))
mtn.draw(window)

mtn2 = Polygon(Point(0.5,0.2),Point(0.75,0.65),Point(1.2,0.2))
mtn2.setFill(color_rgb(205,133,63))
mtn2.draw(window)



#clouds

cloud = Oval(Point(0.75,0.75),Point(0.9,0.83))
cloud.setFill("white")
cloud.setOutline("white")
cloud.draw(window)

cloud2 = Oval(Point(0.55,0.65),Point(0.7,0.68))
cloud2.setFill("white")
cloud2.setOutline("white")
cloud2.draw(window)


cloud3 = Oval(Point(0.35,0.8),Point(0.48,0.85))
cloud3.setFill("white")
cloud3.setOutline("white")
cloud3.draw(window)




#flowers with random colors

from random import randrange

r = randrange(256)
g = randrange(256)
b = randrange(256)


f1 = Circle(Point(0.2,0.1),0.01)
f1.setFill(color_rgb(r,g,b))
f1.draw(window)

f2 = Circle(Point(0.35,0.16),0.01)
f2.setFill(color_rgb(r,g,b))
f2.draw(window)

f3 = Circle(Point(0.45,0.07),0.01)
f3.setFill(color_rgb(r,g,b))
f3.draw(window)

f4 = Circle(Point(0.68,0.03),0.01)
f4.setFill(color_rgb(r,g,b))
f4.draw(window)

f5 = Circle(Point(0.75,0.12),0.01)
f5.setFill(color_rgb(r,g,b))
f5.draw(window)

f6 = Circle(Point(0.87,0.05),0.01)
f6.setFill(color_rgb(r,g,b))
f6.draw(window)



window.getMouse()
window.close()

