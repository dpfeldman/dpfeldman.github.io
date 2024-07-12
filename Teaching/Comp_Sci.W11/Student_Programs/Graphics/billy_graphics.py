# snowman.py
# This program is designed to create a
# virtual snowman!
#
# January 19th, 2011

from graphics import *

# Window properties
win=GraphWin("Billy's Virtual Snowman", 640, 480)
win.setCoords(0.0,0.0,1.3,1.0)
win.setBackground('black')

# The Head
head=Circle(Point(0.65, 0.75), 0.12)
head.setFill('white')
head.setOutline('white')
head.draw(win)

# Right Arm
rightArm=Line(Point(0.24,0.71), Point(0.65, 0.5))
rightArm.setFill('brown')
rightArm.setOutline('brown')
rightArm.draw(win)

# Left arm
lefttArm=Line(Point(0.65,0.5), Point(1.06, 0.71))
lefttArm.setFill('brown')
lefttArm.setOutline('brown')
lefttArm.draw(win)

# Torso
torso=Circle(Point(0.65, 0.52), 0.16)
torso.setFill('white')
torso.setOutline('white')
torso.draw(win)

# Lower Body
lower=Circle(Point(0.65, 0.25), 0.2)
lower.setFill('white')
lower.setOutline('white')
lower.draw(win)

# Right Eye
rightEye=Circle(Point(0.61, 0.79), 0.016)
rightEye.setFill('black')
rightEye.setOutline('black')
rightEye.draw(win)

# Left Eye
leftEye=rightEye.clone()
leftEye.move(0.08,0)
leftEye.draw(win)

# Button 1
buto1=rightEye.clone()
buto1.move(0.04,-0.21)
buto1.draw(win)

# Button 2
buto2=buto1.clone()
buto2.move(0,-0.1)
buto2.draw(win)

# Button 3
buto3=buto2.clone()
buto3.move(0,-0.13)
buto3.draw(win)

# Button 4
buto4=buto3.clone()
buto4.move(0,-0.1)
buto4.draw(win)

# Button 5
buto5=buto4.clone()
buto5.move(0,-0.1)
buto5.draw(win)

# The main part of the hat
hat=Rectangle(Point(0.55,0.98), Point(0.75, 0.85))
hat.setFill('green')
hat.setOutline('green')
hat.draw(win)

# The ribbon on the hat
blackline=Rectangle(Point(0.55,0.896), Point(0.75,0.85))
blackline.setFill('red')
blackline.setOutline('red')
blackline.draw(win)

# The brim of the hat
brim=Rectangle(Point(0.53,0.85), Point(0.77,0.84))
brim.setFill('green')
brim.setOutline('green')
brim.draw(win)

# The top part of the nose
nose=Polygon(Point(0.65,0.77), Point(0.73,0.75), Point(0.65,0.73))
nose.setFill('orange')
nose.setOutline('orange')
nose.draw(win)

# The bottom part of the nose
nosebutt=Circle(Point(0.65,0.75), 0.02)
nosebutt.setFill('orange')
nosebutt.setOutline('orange')
nosebutt.draw(win)

# Piece of smile 1
smile1=Circle(Point(0.59,0.73), 0.01)
smile1.setFill('black')
smile1.setOutline('black')
smile1.draw(win)

# Piece of smile 2
smile2=smile1.clone()
smile2.move(0.12,0)
smile2.draw(win)

# Piece of smile 3
smile3=smile1.clone()
smile3.move(0.02,-0.03)
smile3.draw(win)

# Piece of smile 4
smile4=smile3.clone()
smile4.move(0.08,0)
smile4.draw(win)

# Piece of smile 5
smile5=smile1.clone()
smile5.move(0.06,-0.04)
smile5.draw(win)

# The snowman's greeting!
greeting=Text(Point(0.975,0.85), "Hi! I'm a Snowman!")
greeting.setFill('white')
greeting.draw(win)

# The prompt to close the window
dismissal=Text(Point(0.28,0.9), "Feel free to click anywhere to close my window!")
dismissal.setFill('white')
dismissal.draw(win)

# Connects the snowman to his speech
speech_line=Line(Point(0.79,0.75), Point(0.975, 0.83))
speech_line.setFill('white')
speech_line.setOutline('white')
speech_line.draw(win)

# The function to close the window
win.getMouse()
win.close()



