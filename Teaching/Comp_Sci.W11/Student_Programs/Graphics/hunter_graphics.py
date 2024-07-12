# hallo_hunter.py
# A program that uses the Graphics.py module to print a picture with a measedge to Dave.
# By: Hunter McAdam, 1-22-11

from graphics import*

window=GraphWin("Graphics Window", 800,800)
window.setBackground(color_rgb(0,0,0))

center=Point(400,400)
circ= Circle(center, 200)
circ.setFill('gray')
circ.draw(window)

circ2= Circle(center, 180)
circ2.setFill('black')
circ2.draw(window)

circ3= Circle(center, 150)
circ3.setFill('red')
circ3.draw(window)

circ4= Circle(center, 30)
circ4.setFill('orange')
circ4.draw(window)

t=Text(Point(100,100), "Hello Dave...")
t.setFace("courier")
t.setSize(20)
t.setStyle("bold")
t.setTextColor('white')
t.draw(window)


