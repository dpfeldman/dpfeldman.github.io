# Example Program for class, Thursday 20 Jan. 2011
# This program shows some of the event-driven
# featurs of Zelle's GraphWin module 
# Discussed in class, Thursday 1/20/11

from graphics import *

# download the module here at
# http://mcsp.wartburg.edu/zelle/python/

window = GraphWin("example window", 400,200)
# create an instanceof the GraphWin class

window.setBackground(color_rgb(200,0,200))

t1 = Text( Point(100,80), "Enter a number:")
t1.draw(window)
query = Entry( Point(200,80), 5)
query.setText("42")
query.draw(window)

t2 = Text( Point(100,120), "Click When Ready")
t2.draw(window)

#wait for a mouse click
window.getMouse()

number = eval(query.getText())



# Compute the square
square = number*number

t3 = Text( Point(150,155), "The square of your number is:")
t4 = Text(Point(310,155),square)
t3.draw(window)
t4.draw(window)

# Graph Win can make multiple windows
# Just think of the possibilities
win2 = GraphWin("Congratulations",300,150)
# This is another instance of the GraphiWin class
greeting = Text(Point(150,76),"Nice Job Entering A Number")
greeting.draw(win2)
t2.setText("Click to Quit")

# close the windows when there is a mouse click
window.getMouse()
window.close()
win2.getMouse()
win2.close()
