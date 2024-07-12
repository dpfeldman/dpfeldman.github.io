
# victor_random_image.py
# This program was created by Victor James Smith on Tuesday February 1, 2011.
# This program will generate a random image using user-supplied restrictions.

from graphics import *
from random import *
from time import sleep

def main():

# GUI
    # Generate GUI window
    guiWin = GraphWin("(Semi)Random Image Generator", 600, 450)
    guiWin.setBackground("black")
    guiWin.setCoords(0.0, 0.0, 4.0, 3.0)
    message = Text(Point(2.0, 1.5), "Welcome to the (Semi)Random Image Generator")
    click = Text(Point(2.0, 0.5), "Click to continue")
    message.setFace("courier")
    message.setSize(16)
    message.setStyle("bold")
    message.setTextColor("white")
    click.setFace("courier")
    click.setSize(12)
    click.setStyle("bold")
    click.setTextColor("white")
    message.draw(guiWin)
    click.draw(guiWin)
    guiWin.getMouse()
    message.setText("This program will generate images composed of\ncircles and lines.")
    guiWin.getMouse()
    message.setText("")
    click.setText("Click to generate images")

    # Prompt for informations
    text_circles = Text(Point(1.5, 2.25), "Number of circles per image:")
    input_circles = Entry(Point(3.0, 2.25), 4)
    text_lines = Text(Point(1.5, 1.75), "Number of lines per image:  ")
    input_lines = Entry(Point(3.0, 1.75), 4)
    text_images = Text(Point(1.5, 1.25), "Number of images generated: ")
    input_images = Entry(Point(3.0, 1.25), 4)
    text_circles.setFace("courier")
    text_circles.setSize(14)
    text_circles.setStyle("bold")
    text_circles.setTextColor("white")
    text_lines.setFace("courier")
    text_lines.setSize(14)
    text_lines.setStyle("bold")
    text_lines.setTextColor("white")
    text_images.setFace("courier")
    text_images.setSize(14)
    text_images.setStyle("bold")
    text_images.setTextColor("white")
    text_circles.draw(guiWin)
    input_circles.draw(guiWin)
    text_lines.draw(guiWin)
    input_lines.draw(guiWin)
    text_images.draw(guiWin)
    input_images.draw(guiWin)
    # Wait for mouse click
    guiWin.getMouse()
    guiWin.close()

    # Evaluate inputs
    circles = eval(input_circles.getText())
    lines = eval(input_lines.getText())
    images = eval(input_images.getText())
    
# Images
    for i in range(images):
        # Generate the image window
        iWin = GraphWin("Image Window", 800, 600)
        iWin.setBackground("black")
        iWin.setCoords(0.0, 0.0, 4.0, 3.0)

        # Draw circles
        for i in range(circles):
            x = randrange(5)*random()
                # returns a random x coordinate within grid
            y = randrange(4)*random()
                # returns a random y coordinate within grid
            r = randrange(1, 2)*random()
            circle = Circle(Point(x, y), r)
            circle.setFill(color_rgb(randrange(126, 0, -1), 255, randrange(0, 126)))
                # circle fill limited to green spectrum
            circle.setOutline(color_rgb(randrange(256, 126, -1), 0, randrange(126, 256)))
                # circle outline limited to purple spectrum
            circle.setWidth(randrange(1, 5))
            circle.draw(iWin)
            sleep(0.5*random())

        # Draw lines
        for i in range(lines):
            x1 = randrange(5)*random()
            x2 = randrange(5)*random()
            y1 = randrange(4)*random()
            y2 = randrange(4)*random()
            line = Line(Point(x1, y1), Point(x2, y2))
            line.setFill(color_rgb(randrange(256, 126, -1), 0, randrange(126, 256)))
                # line fill limited to purple spectrum
            line.setWidth(randrange(1, 4))
            line.draw(iWin)
            sleep(0.5*random())
        
    # Wait for a clicks to exit
    iWin.getMouse()
    iWin.close()

main()

