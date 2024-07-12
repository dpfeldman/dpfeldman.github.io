# HAL9000
# by Rory Ives
# Due January 23rd, 2011
#
# Creates a simple graphical likeness to that of
# the computer from Kubrick's 2001: A Space Odyssey
# and then is troublesome when you wish to close it.

from graphics import *

win = GraphWin("Hal9000", 300, 600)
win.setBackground(color_rgb(222, 225, 221))
win.setCoords(0.0, 0.0, 1.0, 1.0)
# Defines the basics of the graphical window.

bgbox = Rectangle(Point(0.05, 0.975), Point(0.95, 0.025))
bgbox.setFill(color_rgb(19,21,19))
bgbox.draw(win)
# Creates the black part of Hal

smbox = Rectangle(Point(0.025, 0.25), Point(0.975, 0.0125))
smbox.setFill(color_rgb(195, 201, 196))
smbox.setOutline(color_rgb(222, 225, 221))
smbox.setWidth(20)
smbox.draw(win)
# Creates Hal's speaker

eye = Oval(Point(0.15, 0.65), Point(0.85, 0.3))
eye.setFill('red')
eye.setOutline(color_rgb(222, 225, 221))
eye.setWidth(20)
eye.draw(win)
# Creates the main redness of Hal's "eye"

light = Oval(Point(0.45, 0.505), Point(0.55, 0.45))
light.setFill('yellow')
light.setOutline(color_rgb(255, 210, 24))
light.setWidth(5)
light.draw(win)
# Creates the creepy yellow light within his "eye"


namebg = Rectangle(Point(0.1, 0.95), Point(0.9, 0.85))
namebg.setFill('black')
namebg.draw(win)

namefill = Rectangle(Point(0.125, 0.935), Point(0.5, 0.865))
namefill.setFill(color_rgb(20, 100, 125))
namefill.draw(win)

name = Text(Point(0.40, 0.9), 'HAL')
name.setFace('arial')
name.setSize(20)
name.setTextColor('white')
name.draw(win)

name = Text(Point(0.65, 0.9), '9000')
name.setFace('arial')
name.setSize(20)
name.setTextColor('white')
name.draw(win)
# The previous four objects make up Hal's nametag
    # I did not realize until commenting this that I didn't name
    # the two text points different things, but it didn't seem
    # to get in the way of my end result so I will leave them as such.

win.getMouse()
win2 = GraphWin("", 300, 150)
apology1 = Text(Point(150, 76), "I'm sorry, Dave.")
apology1.draw(win2)
# Creates a second window

win2.getMouse()
win3 = GraphWin("", 300, 150)
apology2 = Text(Point(150, 76), "I'm afraid I can't let you do that.")
apology2.draw(win3)
# Creates a third window

win3.getMouse()
win3.close()
# Closes the third window

win2.getMouse()
win2.close()
# Closes the second window

win.getMouse()
win.close()
# Closes the first window
