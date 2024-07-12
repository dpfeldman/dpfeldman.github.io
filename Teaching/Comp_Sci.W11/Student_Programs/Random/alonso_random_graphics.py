# alonso_homework4_twowindows.py
#
# This progrm uses creates an image using
# numerical input from the user as well
# as randomly generated numbers.

from graphics import *
from random import randrange
from time import sleep

def main():

    # Create the 2 windows.
    win1 = GraphWin("Create an Image", 300, 300)
    win1.setCoords(0,0,100,100)
    win1.setBackground('cyan4')

    win2 = GraphWin("Your Image", 300, 300)
    win2.setCoords(0,0,100,100)

    # Create the interface. 
    text1 = Text(Point(40,70),"Welcome! Let's make an image.")
    text1.setFill('white')
    text1.draw(win1)

    text2 = Text(Point(40,50),"What should the background color be?")
    text2.setFill('white')
    text2.draw(win1)
    back = Entry(Point(90,50),5)
    back.draw(win1)

    text3 = Text(Point(40,40), "How many triangles would you like?")
    text3.setFill('white')
    text3.draw(win1)
    tnumber = Entry(Point(85,40),5)
    tnumber.draw(win1)

    text4 = Text(Point(40,20), "Click Here to Start Drawing!")
    text4.setFill('white')
    text4.draw(win1)

    # After getting input, wait for click to process.
    win1.getMouse()
    
    # Process input.
    # First, set background color.
    
    win2.setBackground(back.getText())

    # Build originating triangle with fixed coordinates.
    
    p1 = Point(10,10)
    p2 = Point(20,10)
    p3 = Point(10,20)
    triangle = Polygon(p1,p2,p3)
    

    # Now draw as many clones as user wants.
    # Color and location for new triangles are randomly generated.
    # I have kept the range for the triangles at 75 to so they wont
    # go out of the window.

    for i in range(eval(tnumber.getText())):
        triangle2 = triangle.clone()
        r = randrange(256) 
        g = randrange(256)
        b = randrange(256)
        triangle2.setFill(color_rgb(r,g,b))
        triangle2.move(randrange(75),randrange(75))
        sleep(1)
        triangle2.draw(win2)

    # Print Exit Message.
    text5 = Text(Point(50,50), "Click this Window to Exit Program.")
    text5.draw(win2)

    # Wait for mouse click to exit. 
    win2.getMouse()

    win1.close()
    win2.close()

main()
                   
