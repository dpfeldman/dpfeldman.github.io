# This illustrates a common error when assigning names
# to instances of classes


from graphics import *

# what do you think will happen?
c1 = Circle(Point(25,25), 10)
c2 = c1.clone()
c3 = c1.clone()
c2.move(50,50)
c3.move(30,30)


win = GraphWin()

c1.draw(win)
c2.draw(win)
c3.draw(win)
