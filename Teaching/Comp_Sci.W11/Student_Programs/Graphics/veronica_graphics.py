from graphics import *
#Veronica Maresh
#1/23/2011
#This program uses graphics to make a picture.

win=GraphWin("Pretty Picture",300,300)

circ=Circle(Point(250,250),50)
circ.setFill(color_rgb(0,150,200))
circ.draw(win)

circ2=Circle(Point(150,150), 70)
circ2.setFill(color_rgb(0,170,210,))
circ2.draw(win)

circ3=Circle(Point(50,50),40)
circ3.setFill(color_rgb(0,200,150))
circ3.draw(win)

poly=Polygon(Point(299,10),Point(200,10),Point(299,100))
poly.setFill(color_rgb(200,0,100))
poly.draw(win)

poly2=Polygon(Point(100,100),Point(150,100),Point(150,150),Point(100,150))
poly2.setFill('white')
poly2.draw(win)

poly3=Polygon(Point(150,150),Point(200,150),Point(200,200),Point(150,200))
poly3.setFill('white')
poly3.draw(win)

pretty=Text(Point(150,50),"I'm a pretty picture. XD")
pretty.setSize(15)
pretty.draw(win)

l=Line(Point(10,10),Point(10,260))
l.draw(win)
l2=Line(Point(10,260),Point(260,260))
l2.draw(win)
l3=Line(Point(10,10),Point(25,260))
l3.draw(win)
l4=Line(Point(10,35),Point(50,260))
l4.draw(win)
l5=Line(Point(10,60),Point(75,260))
l5.draw(win)
l6=Line(Point(10,85),Point(100,260))
l6.draw(win)
l7=Line(Point(10,110),Point(125,260))
l7.draw(win)
l8=Line(Point(10,135),Point(150,260))
l8.draw(win)
l9=Line(Point(10,160),Point(175,260))
l9.draw(win)
l10=Line(Point(10,185),Point(200,260))
l10.draw(win)
l11=Line(Point(10,210),Point(225,260))
l11.draw(win)
l12=Line(Point(10,235),Point(250,260))
l12.draw(win)
l13=Line(Point(10,260),Point(260,260))


