"""Random color square spiral.

Draws 449 straight lines on a black background. The first line is 51
pixels long and each line is one pixel longer than the one before it,
up to 499 pixels. After every line the turtle turns right 90.991
degrees: just under one degree more than the 90 degrees that would
close a square. That overshoot leaves each four-line lap almost four
degrees clockwise of the one before, so the growing squares twist into
a round web around a small black square in the middle. Every line gets
its own random RGB color, so the colors change on every run.
"""

import random
import turtle

FIRST_LENGTH = 51
LAST_LENGTH = 499
TURN_ANGLE = 90.991  # Just past a square's corner, so each lap twists.


def random_color():
    """Return a random (red, green, blue) color with 0-255 channels."""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def draw_spiral(pen):
    """Draw the twisted square spiral with one random color per line."""
    for length in range(FIRST_LENGTH, LAST_LENGTH + 1):
        pen.pencolor(random_color())
        pen.forward(length)
        pen.right(TURN_ANGLE)


def main():
    """Draw the spiral and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Random Color Square Spiral")
    screen.bgcolor("black")
    screen.colormode(255)

    pen = turtle.Turtle()
    pen.speed("fastest")
    draw_spiral(pen)

    turtle.done()


if __name__ == "__main__":
    main()
