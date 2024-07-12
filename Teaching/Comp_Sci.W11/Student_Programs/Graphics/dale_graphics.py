# eddie izzard's etchasketch end of the world.

from graphics import *

from time import *

window = GraphWin("window", 500, 500)



house = Rectangle(Point(50, 500), Point(300, 300))
house.draw(window)

door = Rectangle(Point(140, 350), Point(210, 495))
door.draw(window)

doorknob = Circle(Point(200, 425), 5)
doorknob.draw(window)

window1 = Rectangle(Point(70, 350), Point(120, 400))
window1.draw(window)
panes1 = Line(Point(95, 350), Point(95, 400))
panes1.draw(window)
panes2 = Line(Point(70, 375), Point(120, 375))
panes2.draw(window)

window2 = Rectangle(Point(230, 350), Point(280, 400))
window2.draw(window)
panes2_1 = Line(Point(255, 350), Point(255, 400))
panes2_2 = Line(Point(230, 375), Point(280, 375))
panes2_1.draw(window)
panes2_2.draw(window)


roof = Polygon ( Point(50, 300), Point(300, 300), Point(175, 200))
#roof.setFill("black")
roof.draw(window)

sleep(1.5)

flood1 = Text(Point(340, 200), "Remember with your etchasketch when you'd \n done the little picture of the house...")
flood1.draw(window)

sleep(2)

flood1.undraw()

flood2 = Text(Point(340, 200), "...and you'd done the little sunshine at the top...")
flood2.draw(window)

sun = Circle(Point(300,100), 30)
sun.draw(window)
#sun.setFill("yellow")

#circ = Circle(Point(300, 100), 40)
#circ.draw(window)
#cent = circ.getCenter()
#x = cent.getX()
#y = cent.getY()
#print(x)
#print(y)


ray1 = Line(Point(340, 100), Point(380, 100))
ray2 = Line(Point(260, 100), Point(220, 100))
ray3 = Line(Point(300, 140), Point(300, 180))
ray4 = Line(Point(300, 60), Point(300, 20))

ray1.draw(window)
ray2.draw(window)
ray3.draw(window)
ray4.draw(window)

ray5 = Line(Point(321, 134), Point(352, 168))
ray6 = Line(Point(279, 134), Point(239, 168))
ray7 = Line(Point(321, 66), Point(352, 32))
ray8 = Line(Point(279, 66), Point(239, 32))

ray5.draw(window)
ray6.draw(window)
ray7.draw(window)
ray8.draw(window)

sleep(2)

flood2.undraw()

flood3 = Text(Point(340, 200), "...and then you'd try and do a dog down there \n and you'd have to leave vapor trails...")
flood3.draw(window)

sleep(.5)

vapor_trail = Line(Point(321, 66), Point(378, 5))
vapor_trail.draw(window)

sleep(.5)

vapor_trail2 = Line(Point(378, 5), Point(500, 5))
vapor_trail2.draw(window)

sleep(.5)

vapor_trail3 = Line(Point(500, 5), Point(500, 300))
vapor_trail3.draw(window)

sleep(.5)

vapor_trail4 = Line(Point(500, 300), Point(500, 500))
vapor_trail4.draw(window)

sleep(2)

blank = Rectangle(Point(0, 500), Point(500, 0))
blank.setFill("grey")
blank.draw(window)


flood5 = Text(Point(250, 250), "Oh, bugger it!")
flood5.draw(window)

window.getMouse()
window.close()


#flood1 = Text(Point(300, 200), "You know when you've drawn the house")
#flood1.draw(window)
             
#Where you've drawn the sun and you go to draw the dog next to the house and
# you have to leave vapor trails around the edge

#house = Rectangle(Point(50, 500), Point(300, 300))
#house.setFill("green4")
#house.draw(window)


#roof = Polygon ( Point(50, 300), Point(300, 300), Point(175, 200))
#roof.setFill("black")
#roof.draw(window)


