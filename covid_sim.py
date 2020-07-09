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

#border draw
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(xmax,ymax)
t.seth(270)

#draw
t.pendown()
t.forward(ymax * 2)
t.right(90)
t.forward(xmax * 2)
t.right(90)
t.forward(ymax * 2)
t.right(90)
t.forward(xmax * 2)
t.right(90)


def initTurt(color="grey"):
    t = turtle.Turtle()

    #misc settings
    t.speed(0)
    t.penup()

    #appearance
    t.shape("circle")
    t.color(color)
    t.turtlesize(1,1,1)

    #positition / orientation
    t.goto(random.randint(-xmax, xmax), random.randint(-ymax, ymax))
    t.seth(random.randint(0,360))
    # t.goto(0,0)
    # t.seth(280)
    return t

def initNTurts(n):
    return [initTurt() for _ in range(n)]

def turtsForward(turts, distance):
    for turt in turts:
        turt.forward(distance)

def turtsWallCheck(turts):
    turt: turtle.Turtle
    for turt in turts:
        if turt.xcor() <= -xmax: #left wall
            delta = turt.heading() - 180
            turt.seth(-delta)
        if turt.xcor() >= xmax: #right wall
            delta = turt.heading()
            turt.seth(180-delta)
        if turt.ycor() <= -ymax: #bottom wall
            delta = turt.heading() - 270
            turt.seth(90-delta)
        if turt.ycor() >= ymax: #top wall
            delta = turt.heading() - 90
            turt.seth(270-delta)

def distance(x0,y0,x1,y1):
    return math.sqrt(((x0 - x1) ** 2) + ((y0 - y1) ** 2))

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
            turt0: turtle.Turtle
            turt1: turtle.Turtle
            turt0, turt1 = turts[i], turts[j]
            if distance(turt0.xcor(), turt0.ycor(), turt1.xcor(), turt1.ycor()) < delta:
                collide(turt0, turt1)

turts = initNTurts(50)
turts.append(initTurt("red"))

while True:
    turtsForward(turts,10)
    turtsWallCheck(turts)
    turtsCollissionCheck(turts, 25)
    s.update()

