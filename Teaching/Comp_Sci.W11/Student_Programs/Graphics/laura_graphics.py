#Laura Zuckerman
#homework assignment 3
#January 23, 2011
#Draw a picture using multiple graphics objects
#This is a picture of a snowman with butt flames
#and text that says "Your tuchus is on fire hotsauce.
#you should really buy some."

from graphics import *

def main ():
    win = GraphWin("My Snowman", 800, 500)
#SKY
#color of the sky: bluish gray
    win.setBackground(color_rgb(200, 196, 222))
#SNOW
#draw a rectangle and fill it in white to
#make the snow
    p1 = Point(0, 370)
    p2 = Point(800, 500)
    snow = Rectangle(p1, p2)
    snow.setFill('white')
    snow.draw(win)
#BOTTOM
 #draw the bottom snowball   
    c = Circle(Point(400,450), 100)
    c.setFill('white')
    c.draw(win)
#MIDDLE
#draw the middle snowball
    c2 = Circle (Point (400, 300), 70)
    c2.setFill ('white')
    c2.draw(win)
#HEAD
#draw the top snowball (head)
    c3 = Circle (Point (400, 190), 50)
    c3.setFill ('white')
    c3.draw (win)
#ARMS
#left arm
    p1 = Point(345, 300) #near body
    p2 = Point(200, 260)
    l = Line (p1,p2)
    l.setWidth(5)
    l.draw(win)
    #left lower finger
    pinky1 = Point(217, 267)#att. arm
    pinky2 = Point(201, 275)
    pinky = Line(pinky1, pinky2)
    pinky.setWidth(3)
    pinky.draw(win)
    #left upper finger
    p6 = Point(228, 267) #att. arm
    p7 = Point(205, 250)
    thumb = Line(p6,p7)
    thumb.setWidth(3)
    thumb.draw(win)

#right arm
    p3 = Point (455, 300)#att. body
    p4 = Point (590, 260)
    l2 = Line (p3, p4)
    l2.setWidth(5)
    l2.draw(win)
    #right lower finger
    rpinky1 = Point(592, 275)
    rpinky2 = Point(576, 267)#att. arm
    pinky = Line(rpinky1, rpinky2)
    pinky.setWidth(3)
    pinky.draw(win)
    #right upper finger
    p6 = Point(585, 250) #att. arm
    p7 = Point(563, 266)
    thumb = Line(p6,p7)
    thumb.setWidth(3)
    thumb.draw(win)
#EYES
#draw the eyes, using a clone
    #left eye
    eye1 = Circle (Point (370, 180), 7)
    eye1.setFill ('black')
    eye2 = eye1.clone()
    #right eye
    eye2.move(25, 0)
    #draw eyes
    eye1.draw(win)
    eye2.draw(win)
#MOUTH
#draw mouth using an oval
    p1 = Point(370, 200)
    p2 = Point(390, 225)
    mouth = Oval(p1, p2)
    mouth.setFill ('black')
    mouth.draw(win)
#FLAME
#draw the flame using an outlined polygon
    #save drawn points in case tinkering
    #needs to happen
    p1 = Point(495, 420)
    p1.draw(win)
    p2 = Point(565, 320)
    p2.draw(win)
    p3 = Point(555, 365)
    p3.draw(win)
    p5 = Point(572, 385)
    p5.draw(win)
    p4 = Point(600, 350)
    p4.draw(win)
    p7 = Point(495, 460)
    p7.draw(win)
    p6 = Point(610, 370)
    p6.draw(win)
    flame = Polygon(p1, p2, p3, p4, p5, p6, p7)
    #set interior to yellow
    flame.setFill('yellow')
    #outline in red
    flame.setWidth(20)
    flame.setOutline('red')
    flame.draw(win)
    #shift to the left because of outline
    flame.move(10, 0)
#HAT
#draw brim of hat - flying off of head
    p1 = Point(450, 100)
    p2 = Point(492, 157)
    l3 = Line(p1, p2)
    l3.setWidth(7)
    l3.draw(win)
#draw body of hat using polygon
    #to make hat angled
    p1 = Point(455, 110)
    p3 = Point(525, 120)
    p2 = Point(497, 80)
    p4 = Point(488, 145)
    hat = Polygon(p1, p2, p3, p4)
    hat.draw(win)
    hat.setFill('black')
#SLOGAN
    #draw title
    anchorPoint = Point(225, 50)
    slogan = Text(anchorPoint, "'Your Tuchus Is On Fire' hotsauce.")
    slogan.draw(win)
    slogan.setFace('times roman')
    slogan.setSize(20)
    #draw subtext          
    anchorPoint = Point(210, 85)
    slogan2 = Text(anchorPoint, "You should really buy some.")
    slogan2.draw(win)
    slogan2.setFace('courier')
    slogan2.setSize(12)
 
main ()


