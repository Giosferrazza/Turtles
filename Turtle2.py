
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
while x <200:
    t.right(30)
    t.color("red")
    t.left(160)
    t.color("orange")
    t.circle(40)
    t.color("yellow")
    t.circle(60)
    t.color("green")
    t.circle(80)
    t.color("blue")
    t.circle(100)
    t.color("indigo")
    t.circle(120)
    t.color("violet")
    t.circle(140)
    x += 10

time.sleep(3)
