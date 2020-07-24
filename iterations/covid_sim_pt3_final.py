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

def initNTurts(n):
    return [initTurt() for _ in range(n)]

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
    angle0, angle1 = turt0.heading(), turt1.heading()
    turt0.seth(angle1)
    turt1.seth(angle0)

    if turt0.color()[0] == "red" or turt1.color()[0] == "red":
        turt0.color("red")
        turt1.color("red")

def turtsCollissionCheck(turts, delta):
    for i in range(len(turts)):
        for j in range(i + 1, len(turts)):
            turt0, turt1 = turts[i], turts[j]
            if turt0.distance(turt1) < delta:
                collide(turt0, turt1)

turts = initNTurts(50)
turts.append(initTurt(color="red"))

while True:
    turtsForward(turts,10)
    turtsWallCheck(turts)
    turtsCollissionCheck(turts, 15)
    s.update()

