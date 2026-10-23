"""Red circle vortex.

Draws 500 pairs of red circles on a black background. At each step
the turtle draws two circles that touch at its position: one with a
radius equal to the step number (0 to 499 pixels) and one three
quarters that size. It then turns right 3 degrees and moves 3 pixels
forward, so over the whole run it walks just over four laps around a
small circle about 115 pixels across. Every circle sits outside that
path and only touches it, so the ever-larger circles pile up into a
red tunnel around a round black hole that no line crosses.
"""

import turtle

STEP_COUNT = 500
INNER_SCALE = 0.75
TURN_ANGLE = 3
STEP_DISTANCE = 3


def draw_vortex(pen):
    """Draw the touching circle pairs while walking around the hole."""
    for radius in range(STEP_COUNT):
        pen.circle(radius)
        pen.circle(radius * INNER_SCALE)
        pen.right(TURN_ANGLE)
        pen.forward(STEP_DISTANCE)


def main():
    """Draw the vortex and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Red Circle Vortex")
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.hideturtle()
    pen.color("red")
    draw_vortex(pen)

    turtle.done()


if __name__ == "__main__":
    main()
