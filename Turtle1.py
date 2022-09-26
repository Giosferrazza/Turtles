
from multiprocessing.connection import wait
import time
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("green")
t.speed(30)
t.pensize(1)
t.goto(-90.00, 0.00)
t.clear()

x = 10
while x < 500:
    t.right(30)
    t.forward(200)
    t.color("red")
    t.left(160)
    t.forward(90)
    t.color("yellow")
    t.circle(20)
    t.color("orange")
    t.circle(30)
    
    x += 10
