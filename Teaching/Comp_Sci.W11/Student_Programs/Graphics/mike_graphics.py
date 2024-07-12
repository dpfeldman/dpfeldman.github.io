#Michael Jenks
#January 22,2011
#This will make a frog pop up in a little box

#I decided to use the definition ability a lot because it made finding
#and stacking the chunks very easy


from graphics import *

window = GraphWin("My Frog")

def left():
#this is the left eye
    c= Point(50,60)
    circ=Circle(c,20)
    circ.setFill("yellow")
    circ.draw(window)

    c=Point(50,60)
    circ2=Circle(c,3)
    circ2.setFill("blue")
    circ2.draw(window)


def right():
#this is the right eye
    c= Point(100,60)
    circ=Circle(c,20)
    circ.setFill("yellow")
    circ.draw(window)

    c=Point(100,60)
    circ2=Circle(c,3)
    circ2.setFill("blue")
    circ2.draw(window)

def head():
    semi=Oval(Point(20,40),Point(130,100))
    semi.setFill("green")
    semi.draw(window)

def tongue():
    ton=Polygon(Point(60,90),Point(70,92),Point(175,150),Point(80,92),Point(90,90))
    ton.setFill("red")
    ton.draw(window)

def body():
    bod=Oval(Point(10,35),Point(140,130))
    bod.setFill("green")
    bod.draw(window)

def legs():
    Lleg=Rectangle(Point(40,100),Point(60,140))
    Rleg=Lleg.clone()
    Rleg.move(50,0)
    Lleg.setFill("green")
    Rleg.setFill("green")
    Lleg.draw(window)
    Rleg.draw(window)
#the feet circles
    Lcirc=Circle(Point(50,150),15)
    Lcirc.setFill("green")
    Rcirc=Lcirc.clone()
    Rcirc.move(50,0)
    Rcirc.draw(window)
    Lcirc.draw(window)

def toes():
    first=Circle(Point(40,160),6)
#I found the clone option quite useful
    second=first.clone()
    third=first.clone()
    fourth=first.clone()
    fifth=first.clone()
    sixth=first.clone()

    second.move(11,5)
    third.move(22,0)
    fourth.move(50,0)
    fifth.move(61,5)
    sixth.move(72,0)

    first.setFill("orange")
    second.setFill("orange")
    third.setFill("orange")
    fourth.setFill("orange")
    fifth.setFill("orange")
    sixth.setFill("orange")
    
    first.draw(window)
    second.draw(window)
    third.draw(window)
    fourth.draw(window)
    fifth.draw(window)
    sixth.draw(window)

def hindlegs():
#The hind legs were very difficult to draw because the polygon pieces can get quite complicated
#I would suggest playing with the polygons because they are so difficult to use
    lefty=Polygon(Point(50,120),Point(15,130),Point(50,130),Point(40,150),Point(0,130),Point(40,50))
    righty=Polygon(Point(100,120),Point(135,130),Point(110,135),Point(120,145),Point(150,130),Point(110,50))
    righty.setFill("green")
    lefty.setFill("green")
    righty.draw(window)
    lefty.draw(window)
    first_foot=Circle(Point(35,140),15)
    second_foot=first_foot.clone()
    second_foot.move(75,0)
    second_foot.setFill("green")
    first_foot.setFill("green")
    second_foot.draw(window)
    first_foot.draw(window)
#The toes on the hind legs
    toe_one=Circle(Point(25,150),6)

    toe_two=toe_one.clone()
    toe_three=toe_one.clone()
    toe_four=toe_one.clone()

    toe_three.move(97,0)
    toe_four.move(87,5)
    toe_two.move(10,5)

    toe_one.setFill("orange")
    toe_two.setFill("orange")
    toe_three.setFill("orange")
    toe_four.setFill("orange")

    toe_two.draw(window)
    toe_one.draw(window)
    toe_three.draw(window)
    toe_four.draw(window)

def bug():
#I just figured that the frog needed a snack
    wing_one=Circle(Point(173,150),4)
    wing_two=wing_one.clone()
    wing_two.move(4,-5)
    wing_one.setFill("yellow")
    wing_two.setFill("yellow")
    wing_two.draw(window)
    bugg=Circle(Point(175,150),6)
    bugg.setFill("black")
    bugg.draw(window)
    wing_one.draw(window)



#Notice what happens if you change the order of the functions
# i.e. switch body() and head()
hindlegs()
legs()
toes()
body()
head()
tongue()
right()
left()
bug()


