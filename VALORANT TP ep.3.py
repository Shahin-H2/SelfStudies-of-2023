import colorsys
import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")

t.penup()
t.goto(-200,-100)
t.pendown()
t.speed(10)

a=400
h=0
n=100

def triangle():
    global a,n,h
    for i in range(40):
        c = colorsys.hsv_to_rgb(h,1,0.7)
        h=h+(1/n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a=a-10

triangle()
triangle()

t.hideturtle()
turtle.done()