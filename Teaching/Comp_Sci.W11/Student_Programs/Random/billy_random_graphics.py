# billy_random_graphics.py
# This program is designed to create random
# shapes and random colors.
#
# January 27th, 2011

from graphics import *
from random import randrange
from time import sleep

def main():
    # Color properties for Random Graphics Drawing Window
    random_color=color_rgb(randrange(256), randrange(256), randrange(256))

    # User Interface Window
    user_win=GraphWin("Random Graphics User Interface", 400, 300)
    user_win.setCoords(0.0, 0.0, 40, 30)
    user_win.setBackground('black')

    # Greeting
    hello=Text(Point(20,27), "\nHello! I am a shape drawing program!\n\nI'm designed to color, size and stretch various shapes!\n\n(As many as you want!)")
    hello.setTextColor('yellow')
    hello.draw(user_win)
    
    # User input (circles)
    circ_text=Text(Point(20,20), "How many circles would you like for me to draw?:")
    circ_text.setTextColor('white')
    circ_text.draw(user_win)
    circ_query=Entry(Point(20,18), 2)
    circ_query.setText("0")
    circ_query.draw(user_win)

    # User input (rectangles)
    rect_text=Text(Point(20,14), "How many rectangles?:")
    rect_text.setTextColor('white')
    rect_text.draw(user_win)
    rect_query=Entry(Point(20,12), 2)
    rect_query.setText("0")
    rect_query.draw(user_win)

    # User input (triangles
    tri_text=Text(Point(20,8), "How many triangles?:")
    tri_text.setTextColor('white')
    tri_text.draw(user_win)
    tri_query=Entry(Point(20,6), 2)
    tri_query.setText("0")
    tri_query.draw(user_win)

    # This is the prompt to run the rest of the program
    prompt=Text(Point(20,2), "Click anywhere in this window to run me!")
    prompt.setTextColor('red')
    prompt.draw(user_win)
    user_win.getMouse()

    # This makes the user input compatible with the Random Graphics Window
    circ=eval(circ_query.getText())
    rect=eval(rect_query.getText())
    tri=eval(tri_query.getText())

    # Drawing Window
    visual_win=GraphWin("Random Graphics Drawing Window", 400, 300)
    visual_win.setCoords(0.0, 0.0, 40, 30)
    visual_win.setBackground(random_color)

    # Circle properties and Loop
    for i in range(circ):
        random_color2=color_rgb(randrange(256), randrange(256), randrange(256))
        random_color3=color_rgb(randrange(256), randrange(256), randrange(256))
        circ=Circle(Point(randrange(40), randrange(30)), randrange(7))
        circ.setFill(random_color2)
        circ.setOutline(random_color3)
        sleep(1)
        circ.draw(visual_win)

    # Rectangle properties and Loop
    for i in range(rect):
        random_color4=color_rgb(randrange(256), randrange(256), randrange(256))
        random_color5=color_rgb(randrange(256), randrange(256), randrange(256))
        rect=Rectangle(Point(randrange(40), randrange(30)), Point(randrange(40), randrange(30)))
        rect.setFill(random_color4)
        rect.setOutline(random_color5)
        sleep(1)
        rect.draw(visual_win)

    # Triangle properties and Loop
    for i in range(tri):
        random_color6=color_rgb(randrange(256), randrange(256), randrange(256))
        random_color7=color_rgb(randrange(256), randrange(256), randrange(256))
        tri=Polygon(Point(randrange(40), randrange(30)), Point(randrange(40), randrange(30)), Point(randrange(40), randrange(30)))
        tri.setFill(random_color6)
        tri.setOutline(random_color7)
        sleep(1)
        tri.draw(visual_win)

    # Farewell and clear user screen
    hello.setText("\n\nThank you for allowing me to express my creativity!\n\nPlease feel free to come back if you want me\n\nto draw even more random shapes and colors!")
    circ_text.setText("")
    circ_query.setText("")
    rect_text.setText("")
    rect_query.setText("")
    tri_text.setText("")
    tri_query.setText("")
    prompt.setText("Click anywhere in this window to exit")

    # Close both windows with one click (in user interface window)
    user_win.getMouse()
    user_win.close()
    visual_win.close()
    
main()

