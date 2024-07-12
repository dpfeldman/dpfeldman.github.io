#HW3_LisaBjerke_Graphics_Rainbow
#make a blue sky
#make a rainbow
#make rain
#make a sun

from graphics import *
win1 = GraphWin("Lisa_Bjerke_Graphic", 500,350)
win1.setBackground("blue")


#Sun
circ = Circle( Point(110,80), 50)
circ.setFill('yellow')
circ.draw(win1)

win1.getMouse()

#Plus sign
p1=Point(200, 80)
p2=Point(300, 80)
l1=Line(p1, p2)
l1.setWidth(5)
l1.draw(win1)

p3=Point(250, 40)
p4=Point(250, 120)
l2=Line(p3, p4)
l2.setWidth(5)
l2.draw(win1)

win1.getMouse()

#Rain
#Clone
rain0=Circle(Point(250, 150), 10)
rain0.setFill("light blue")
rain0.draw(win1)

rain1=rain0.clone()
rain1.move(50, 50)
rain1.draw(win1)

rain2=rain0.clone()
rain2.move(-100, 100)
rain2.draw(win1)

rain3=rain0.clone()
rain3.move(-200, -40)
rain3.draw(win1)

rain4=rain0.clone()
rain4.move(180, -75)
rain4.draw(win1)

rain5=rain0.clone()
rain5.move(190, -30)
rain5.draw(win1)

rain6=rain0.clone()
rain6.move(-135, 20)
rain6.draw(win1)

rain7=rain0.clone()
rain7.move(-120, -120)
rain7.draw(win1)

rain8=rain0.clone()
rain8.move(80, -20)
rain8.draw(win1)

rain9=rain0.clone()
rain9.move(170, 40)
rain9.draw(win1)

rain10=rain0.clone()
rain10.move(40, 160)
rain10.draw(win1)

rain11=rain0.clone()
rain11.move(80, 20)
rain11.draw(win1)

rain12=rain0.clone()
rain12.move(140, 100)
rain12.draw(win1)

rain13=rain0.clone()
rain13.move(140,60)
rain13.draw(win1)

win1.getMouse()

#equals:

p5=Point(200, 250)
p6=Point(250, 250)
l3=Line(p5, p6)
l3.setWidth(5)
l3.draw(win1)

l4=l3.clone()
l4.move(0,40)
l4.draw(win1)

win1.getMouse()
win1.close()

#Win2 with rainbow
win2 = GraphWin("Lisa_Bjerke_Graphic", 1000,700)
win2.setBackground("blue")

#Rainbow
red= Circle( Point(500,800),600)
red.setFill("red")
red.draw(win2)

organge= Circle( Point(500,850),580)
organge.setFill("orange")
organge.draw(win2)

yellow= Circle( Point(500,900),560)
yellow.setFill("yellow")
yellow.draw(win2)

green= Circle( Point(500,950),540)
green.setFill("green")
green.draw(win2)

light_blue= Circle( Point(500,1000),520)
light_blue.setFill("light blue")
light_blue.draw(win2)

dark_blue= Circle( Point(500,1050),500)
dark_blue.setFill("dark blue")
dark_blue.draw(win2)

purple= Circle( Point(500,1100),480)
purple.setFill("purple")
purple.draw(win2)

blue= Circle( Point(500,1150),460)
blue.setFill("blue")
blue.draw(win2)

#Close
win2.getMouse()
win2.close()

