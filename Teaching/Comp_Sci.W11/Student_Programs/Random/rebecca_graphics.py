# Rebecca Coombs
# graphics package
# random shapes & colors
# two GraphWin windows - one for pictures
#                   - one for info and input boxes (total shapes, size range)
# setCoords
# getMouse()



from graphics import *

from random import random

    #input window
window = GraphWin("Create Your Own Design", 400,300)
window.setCoords(0.0, 0.0, 10.0, 10.0)
window.setBackground(color_rgb(46,139,87))

    #greeting
t1 = Text(Point(5,9),"ENTER GRAPHICS INFORMATION")
t1.draw(window)

    # number of circles
t2 = Text( Point(4,7),"Enter number of circles between 0 and 10:")
t2.draw(window)
query = Entry( Point(8,7),4)
query.setText("3")
query.draw(window)


t3 = Text(Point(4,5), "Enter red color value for background (0-256):")
t3.draw(window)
query2 = Entry(Point(8,5),4)
query2.setText("150")
query2.draw(window)

t4 = Text(Point(4,4), "Enter green color value for background (0-256):")
t4.draw(window)
query3 = Entry(Point(8,4),4)
query3.setText("150")
query3.draw(window)

t5 = Text(Point(4,3), "Enter blue color value for background (0-256):")
t5.draw(window)
query4 = Entry(Point(8,3),4)
query4.setText("150")
query4.draw(window)


t6 = Text (Point(5,2),"Click when ready")
t6.draw(window)



#eval for later use
window.getMouse()
n_o_c = eval(query.getText())
r_background = eval(query2.getText())
g_background = eval(query3.getText())
b_background = eval(query4.getText())



window.getMouse()
window.close()




    #graphics window
window = GraphWin("Your Design", 500,500)
window.setCoords(0.0, 0.0, 1.0, 1.0)
window.setBackground(color_rgb(r_background,g_background,b_background))

    #randomize circle coordinates
x = random()
y = random()
    
x2 = random()
y2 = random()
    
x3 = random()
y3 = random()

x4 = random()
y4 = random()

x5 = random()
y5 = random()

x6 = random()
y6 = random()

x7 = random()
y7 = random()

x8 = random()
y8 = random()

x9 = random()
y9 = random()

x10 = random()
y10 = random()


#random colors for circles

from random import randrange

r = randrange(256)
g = randrange(256)
b = randrange(256)

c1 = Circle(Point(x,y),.1)
c1.setFill(color_rgb(r,g,b))
c2 = Circle(Point(x2,y2),.1)
c2.setFill(color_rgb(r,g,b))
c3 = Circle(Point(x3,y3),.1)
c3.setFill(color_rgb(r,g,b))
c4 = Circle(Point(x4,y4),.1)
c4.setFill(color_rgb(r,g,b))
c5 = Circle(Point(x5,y5),.1)
c5.setFill(color_rgb(r,g,b))
c6 = Circle(Point(x6,y6),.1)
c6.setFill(color_rgb(r,g,b))
c7 = Circle(Point(x7,y7),.1)
c7.setFill(color_rgb(r,g,b))
c8 = Circle(Point(x8,y8),.1)
c8.setFill(color_rgb(r,g,b))
c9 = Circle(Point(x9,y9),.1)
c9.setFill(color_rgb(r,g,b))
c10 = Circle(Point(x10,y10),.1)
c10.setFill(color_rgb(r,g,b))


#number of circles from input window
z = n_o_c

    

for i in range(z):
    if z == 1:
        c1.draw(window)
    if z ==2:
        c1.draw(window)
        c2.draw(window)
    if z == 3:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
    if z == 4:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
    if z == 5:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
        c5.draw(window)
    if z == 6:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
        c5.draw(window)
        c6.draw(window)
    if z == 7:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
        c5.draw(window)
        c6.draw(window)
        c7.draw(window)
    if z == 8:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
        c5.draw(window)
        c6.draw(window)
        c7.draw(window)
        c8.draw(window)
    if z == 9:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
        c5.draw(window)
        c6.draw(window)
        c7.draw(window)
        c8.draw(window)
        c9.draw(window)
    if z == 10:
        c1.draw(window)
        c2.draw(window)
        c3.draw(window)
        c4.draw(window)
        c5.draw(window)
        c6.draw(window)
        c7.draw(window)
        c8.draw(window)
        c9.draw(window)
        c10.draw(window)
            
# is there a quicker way to include all 'draws' from the previous 'if' plus one more?




window.getMouse()
window.close()

