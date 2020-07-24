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
        if turt.xcor() < -xmax: #left wall
            delta = turt.heading() - 180
            turt.seth(-delta)
            turt.setx(-xmax)
        if turt.xcor() > xmax: #right wall
            delta = turt.heading()
            turt.seth(180-delta)
            turt.setx(xmax)
        if turt.ycor() < -ymax: #bottom wall
            delta = turt.heading() - 270
            turt.seth(90-delta)
            turt.sety(-ymax)
        if turt.ycor() > ymax: #top wall
            delta = turt.heading() - 90
            turt.seth(270-delta)
            turt.sety(ymax)

def collide(turt0, turt1):
    #######################################################################
    # hint: functions turt0.heading(), turt1.heading() turt0.seth(_angle_) turt1.seth(_angle_)
    # hint: functions turt0.color(_color_) - changes the color of turt0 to _color_
    # just calling turt0.color() returns the current color of turt0 (note the parantheses are empty)
    angle0, angle1 = turt0.heading(), turt1.heading()
    turt0.seth(angle1)
    turt1.seth(angle0)

    #bonus:
    if turt0.color()[0] == "red" or turt1.color()[0] == "red":
        turt0.color("red")
        turt1.color("red")
    #######################################################################
    

turts = [initTurt(x=100, y=0, angle=0, color="blue"),
         initTurt(x=-100, y=0, angle=180, color="green")]

while True:
    turtsForward(turts,2)
    turtsWallCheck(turts)
    #########################################
    #need and IF case Hint the (turts[0].distance(turts[1]) might help)
    if turts[0].distance(turts[1]) < 20:
        collide(turts[0], turts[1])
    #########################################
    s.update()

