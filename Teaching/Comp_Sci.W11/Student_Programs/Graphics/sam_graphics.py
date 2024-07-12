# this is a drawing

from graphics import *

win = GraphWin("Click to Close", 400,200)

#back ground

frontier = Rectangle(Point(0,0), Point(400,200))
frontier.setFill ("Black")
frontier.draw(win)

#this is the background planet
 
bplanet = Circle(Point(55,151), 30)
bplanet.setFill ("red3")
bplanet.draw(win)

#planet in foreground

pcent = Point (298,-20)
planet2 = Circle(pcent, 236)
planet2.setFill (color_rgb(215, 42, 48))
planet2.draw(win)

planet = Circle(pcent, 230)
planet.setFill (color_rgb(242, 102, 13))
planet.draw(win)

crate3 = Oval(Point(90,-34), Point(141,79))

crate3.setFill (color_rgb(215, 42, 48))
crate3.draw(win)
crate4 = Oval(Point(189,149), Point(250,197))
crate4.setFill (color_rgb(215, 42, 48))
crate4.draw(win)
crate5 = Oval(Point(100,12), Point(131,39))
crate5.setFill (color_rgb(215, 42, 48))
crate5.draw(win)
crate15 = Oval(Point(80,22), Point(118,39))
crate15.setFill (color_rgb(242, 102, 18))
crate15.draw(win)
crate5a = crate5.clone()
crate5a.move(33,95)
crate5a.draw(win)
crate1 = Oval(Point(119,49), Point(171,97))
crate1.setFill (color_rgb(215, 42, 48))
crate1.draw(win)
crate2 = Oval(Point(135,59), Point(161,80))
crate2.setFill (color_rgb(242, 102, 13))
crate2.draw(win)
crate6 = Oval(Point(167,99), Point(198,127))
crate6.setFill (color_rgb(242, 102, 13))
crate6.draw(win)
crate7 = Oval(Point(95,114), Point(133,53))
crate7.setFill (color_rgb(215, 42, 48))
crate7.draw(win)
crate8 = Oval(Point(150,135), Point(171,151))
crate8.setFill (color_rgb(215, 42, 48))
crate8.draw(win)

# Ship body

torso = Polygon(Point(189,144), Point(203,150), Point(342,116), Point(310,79), Point(197,123))
torso.setFill (color_rgb(58, 42, 53))
torso.draw(win)

cheek = Polygon(Point(192,154), Point(245,138), Point(240,124), Point(196,145))
cheek.setFill (color_rgb(88, 88, 88))
cheek.draw(win)

shoulder = Polygon(Point(238,123), Point(281,93), Point(284,105), Point(245,137))
shoulder.setFill (color_rgb(154, 109, 129))
shoulder.draw(win)

scap = Polygon(Point(281,93), Point(285,105), Point(314,97), Point(312,85))
scap.setFill (color_rgb(154, 109, 129))
scap.draw(win)

a4 = Rectangle(Point(326,93), Point(360,113))
a4.setFill (color_rgb(39, 29, 40))
a4.draw(win)

neck = Polygon(Point(177,158), Point(190,151), Point(202,128), Point(260,101), Point(251,91), Point(180,120))
neck.setFill (color_rgb(118, 81, 98))
neck.draw(win)

nose = Polygon(Point(162,156), Point(178,158), Point(187,124), Point(180,120))                              
nose.setFill (color_rgb(154, 109, 129))
nose.draw(win)

flap = Polygon(Point(310,85), Point(321,80), Point(329,94), Point(315,97))                              
flap.setFill (color_rgb(154, 109, 129))
flap.draw(win)

back = Polygon(Point(249,90), Point(255,102), Point(312,85), Point(300,79))
back.setFill (color_rgb(118, 81, 98))
back.draw(win)

aft = Polygon(Point(334,77), Point(321,80), Point(329,94), Point(342,89))                              
aft.setFill (color_rgb(154, 109, 129))
aft.draw(win)

poopdeck = Polygon(Point(331,117), Point(329,94), Point(342,89), Point(347,119))                              
poopdeck.setFill (color_rgb(118, 81, 98))
poopdeck.draw(win)

bridge = Polygon(Point(173,135), Point(184,135), Point(181,143), Point(168,145))
bridge.setFill (color_rgb(12, 12, 12))
bridge.draw(win)

tena = Polygon(Point(109,185), Point(201,155), Point(205,151))
tena.setOutline(color_rgb(88, 88, 88))
tena.setFill (color_rgb(118, 81, 98))
tena.draw(win)


#engine thing

arm = Polygon(Point(295,109), Point(314,127), Point(335,118), Point(331,100))                              
arm.setFill (color_rgb(154, 109, 129))
arm.draw(win)

engine = Polygon(Point(313,152), Point(354,138), Point(365,138), Point(380,131), Point(384,121), Point(380,117), Point(319,142))
engine.setFill (color_rgb(39, 29, 40))
engine.draw(win)

a1 = Polygon(Point(319,142), Point(314,134), Point(302,122),  Point(290,120))
a1.setFill (color_rgb(154, 109, 129))
a1.draw(win)

a2 = Polygon(Point(357,129), Point(371,126), Point(384,120),  Point(380,110),  Point(366,102),  Point(349,107),  Point(336,109),  Point(353,119))
a2.setFill (color_rgb(118, 81, 98))
a2.draw(win)
a3 = Polygon(Point(366,102),  Point(349,107),  Point(336,109),  Point(347,101), Point(360,98))
a3.setFill (color_rgb(88, 88, 88))
a3.draw(win)

a5 = Polygon(Point(319,142), Point(313,131), Point(302,122), Point(336,110), Point (353,120), Point(357,129))
a5.setFill (color_rgb(118, 81, 98))
a5.draw(win)

take = Polygon(Point(312,152), Point(319,142), Point(292,121), Point(286,133))
take.setFill (color_rgb(154, 109, 129))
take.draw(win)

iqwen = Polygon(Point(311,148), Point(314,144), Point(294,127), Point(290,132))
iqwen.setFill (color_rgb(12, 12, 12))
iqwen.draw(win)

lid = Polygon(Point(314,134), Point(302,122), Point(337,110), Point(354,120))
lid.setFill (color_rgb(154, 109, 129))
lid.draw(win)
lida = Polygon(Point(293,122), Point(290,120), Point(301,123), Point(337,110), Point(335,108))
lida.setFill (color_rgb(118, 81, 98))
lida.draw(win)

topbacklid = Polygon(Point(349,108), Point(365,103), Point(380,110), Point(365,115))
topbacklid.setFill (color_rgb(154, 109, 129))
topbacklid.draw(win)
t = Line(Point(365,115), Point(371,126))
t.draw(win)
o = Line(Point(365,115), Point(353,120))
o.draw(win)

#to exit
               
win.getMouse()
               
win.close()

