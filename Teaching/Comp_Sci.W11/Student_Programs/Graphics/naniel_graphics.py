# File: naniel_hw3_solarsystem.py
# Nathaniel Hilliard
# January 20, 2011

# This program uses the Graphics import to illustrate the Solar System.

from graphics import *

def main():
      window = GraphWin("example window", 400, 300)
      window.setBackground('black')

      greeting = Text(Point(145, 275), 'Greetings, and welcome to your Solar System')
      greeting.setStyle('bold')
      greeting.setOutline('white')
      greeting.draw(window) 

# The following shapes are the planets and the sun:
   
      sun = Circle(Point(0, 150), 50)
      sun.setFill('yellow')
      sun.draw(window)
      sun_text = Text(Point(25, 150), 'The Sun')
      sun_text.draw(window)
                      
      mercury = Circle(Point(70, 157), 5)
      mercury.setFill('gray')
      mercury.draw(window)
      
      venus = Circle(Point(105, 150), 12)
      venus.setFill('green')
      venus.draw(window)
      
      earth = Circle(Point(140, 148), 12)
      earth.setFill('blue')
      earth.draw(window)
      
      mars = Circle(Point(170, 150), 7)
      mars.setFill('red')
      mars.draw(window)
      
      jupiter = Circle(Point(210, 150), 20)
      jupiter.setFill('orange')
      jupiter.draw(window)
      
      saturn = Circle(Point(260, 150), 13)
      saturn.setFill('green')
      saturn.draw(window)
      saturn_ring = Line(Point(240, 160), Point(280, 140))
      saturn_ring.setOutline('yellow')
      saturn_ring.draw(window)
      
      uranus = Circle(Point(315, 149), 14)
      uranus.setFill('blue')
      uranus.draw(window)
      
      neptune = Circle(Point(370, 150), 11)
      neptune.setFill('gray')
      neptune.draw(window)

# A spaceship
      
      spaceship_body = Rectangle(Point(175, 110), Point(190, 100))
      spaceship_body.setFill('white')
      spaceship_body.draw(window)
      spaceship = Text(Point(180, 80), '(Spaceship)')
      spaceship.setOutline('white')
      spaceship.draw(window)
      spaceship_arrow = Line(Point(180, 85), Point(180, 97))
      spaceship_arrow.setArrow('last')
      spaceship_arrow.setOutline('white')
      spaceship_arrow.draw(window)

# The following is miscellaneous space matter

      poly = Polygon(Point(390, 10), Point(390, 40), Point(370, 25))
      poly.setFill('red')
      poly.draw(window)
      tri = Polygon(Point(200, 120), Point(210, 120), Point(195, 110))
      tri.setFill('yellow')
      tri.draw(window)
      tri2 = Polygon(Point(250, 100), Point(260, 100), Point(245, 120))
      tri2.setFill('yellow')
      tri2.draw(window)
      tri3 = Polygon(Point(150, 170), Point(160, 180), Point(145, 170))
      tri3.setFill('yellow')
      tri3.draw(window)
      tri4 = Polygon(Point(300, 205), Point(310, 205), Point(315, 225))
      tri4.setFill('yellow')
      tri4.draw(window)

main()
      
