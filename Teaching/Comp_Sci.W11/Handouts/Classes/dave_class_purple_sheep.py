# Example to illustrate how to build your own classes
# This is a very powerful technique for structuring
# your programs and making good, readable, and re-usable
# code

# I'm imagining that I want to simulate a system in
# which purple sheep wander around a field 

# My objects are going to be sheep and a field

from random import randrange
from graphics import *
from time import sleep

class Sheep:

    def __init__(self,n): # this is the constructor
        self.xpos = 0
        self.ypos = 0
        self.n = n # n is size of the field

    def move(self): #moves sheep in a random direction
        # the mod functions enforce periodic boundaries
        z = randrange(4)
        if(z==0):
            self.xpos = (self.xpos -1)%self.n
        elif(z==1):
            self.xpos = (self.xpos + 1)%self.n
        elif(z==2):
            self.ypos = (self.ypos - 1)%self.n
        else:
            self.ypos = (self.ypos + 1)%self.n

    def draw(self,field):
        x = self.xpos
        y = self.ypos
        r = Rectangle(Point(x,y), Point(x+1,y+1))
        r.setFill("purple")
        r.draw(field.getWin())
                      

class Field:

    def __init__(self,n):
        self.win = GraphWin("A Field of Sheep", 200,200)
        self.win.setCoords(0,0,n,n)
        r = []
        for x in range(n):
            for y in range(n):
                r = Rectangle(Point(x,y), Point(x+1,y+1))
                r.draw(self.win)

    def close(self):
        (self.win).getMouse()
        (self.win).close()

    def getWin(self):
        return(self.win)

def main():
    n = 10
    alice = Sheep(n)
    alice.move()
    f = Field(n)
    for i in range(100):
        alice.draw(f)
        alice.move()
        sleep(0.1)

    f.close()
main()
    
