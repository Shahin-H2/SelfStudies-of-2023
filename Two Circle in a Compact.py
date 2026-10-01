import turtle
turtle.bgcolor("black")
turtle.speed(25)
turtle.hideturtle()

def rotate ():
    for i in range (500):
        turtle.color("red")
        turtle.circle(i)
        turtle.circle(i*0.75)
        turtle.right(3)
        turtle.forward(3)

rotate ()
turtle.done()