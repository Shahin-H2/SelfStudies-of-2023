"""Rainbow hexagram.

Draws a six-pointed star on a black background from 80 straight
lines, with a 120-degree left turn after each one. The first line is
400 pixels long and every line is 10 pixels shorter than the one
before, so the first 40 lines wind inward as nested triangles pointing
up. The length then reaches zero and keeps shrinking into negative
numbers, which makes the turtle walk backwards: the last 40 lines grow
back out to 390 pixels as nested triangles pointing down, and the two
triangles interlock into a star. Every line nudges the hue one
hundredth of the way around the color wheel, from red through yellow
and green to blue and purple, at 70% brightness.
"""

import colorsys
import turtle

LINE_COUNT = 80
FIRST_LENGTH = 400
LENGTH_STEP = 10
HUE_STEP = 1 / 100
BRIGHTNESS = 0.7


def draw_hexagram(pen):
    """Draw the star as one triangle spiral that shrinks past zero."""
    hue = 0.0
    length = FIRST_LENGTH
    for _ in range(LINE_COUNT):
        pen.color(colorsys.hsv_to_rgb(hue, 1, BRIGHTNESS))
        hue += HUE_STEP
        # Negative lengths back the turtle up, which flips the triangle.
        pen.forward(length)
        pen.left(120)
        length -= LENGTH_STEP


def main():
    """Draw the star and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Rainbow Hexagram")
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.penup()
    # Start low and left so the finished star sits near the center.
    pen.goto(-200, -100)
    pen.pendown()
    pen.speed("fast")
    draw_hexagram(pen)
    pen.hideturtle()

    turtle.done()


if __name__ == "__main__":
    main()
