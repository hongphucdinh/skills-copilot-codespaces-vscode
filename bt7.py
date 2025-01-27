import turtle
import random as r
t = turtle.Turtle()
t.shape("turtle")
t.hideturtle()
t.pensize(3)
t.color("blue")
t.speed(1)
t.penup()
t.goto(-400, 0)
t.showturtle()
count = 0
while count < 10:
    down = r.randint(20, 50)
    up = r.randint(20, 50)
    t.pendown()
    t.forward(down)
    t.penup()
    t.forward(up)
    count += 1
turtle.done()
