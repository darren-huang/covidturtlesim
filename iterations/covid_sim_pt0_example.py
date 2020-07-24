import turtle
import random
import math

#screen setup
dim = 1000
border = 50
xmax, ymax = dim, dim
s = turtle.Screen()
s.screensize((xmax + border) * 2 , (ymax + border) * 2, "white")
s.setworldcoordinates(-xmax-border, -ymax-border, xmax+border, ymax+border)
s.tracer(0)



def initTurt(x=None, y=None, angle=None, color="grey"):
    t = turtle.Turtle()

    #misc settings
    t.speed(0)
    t.penup()

    #appearance
    t.shape("circle")
    t.color(color)

    #positition
    if x == None and y == None:
        t.goto(random.randint(-xmax, xmax), random.randint(-ymax, ymax))
    else:
        t.goto(x,y)

    #orientation
    if angle == None:
        t.seth(random.randint(0,360))
    else:
        t.seth(angle)
    
    return t

def turtsForward(turts, distance):
    for turt in turts:
        turt.forward(distance)

turts = [initTurt(color="red"), initTurt(color="blue")]

while True:
    turtsForward(turts,.5)
    s.update()

