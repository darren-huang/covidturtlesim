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

#make a turtle to draw the border
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(xmax,ymax)
t.seth(270)

#draw the border
t.pendown()
t.forward(ymax * 2)
t.right(90)
t.forward(xmax * 2)
t.right(90)
t.forward(ymax * 2)
t.right(90)
t.forward(xmax * 2)
t.right(90)


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

def turtsWallCheck(turts):
    for turt in turts:
        ############################################################################
        if turt.ycor() > ymax: #top wall
            delta = turt.heading() - 90
            turt.seth(270-delta)
            turt.sety(ymax)
        ############################################################################

turts = [initTurt(x=100, y=0, angle=90, color="red"),
         initTurt(x=-100, y=0, angle=90, color="blue")]

while True:
    turtsForward(turts,2)
    turtsWallCheck(turts)
    s.update()

