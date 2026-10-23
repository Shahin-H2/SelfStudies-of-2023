"""Yellow and red flower.

Draws a dense flower of 480 pointed petals on a black background,
alternating yellow and red. Each petal is two 100-degree arcs: the
turtle sweeps out along the first arc, turns 90 degrees left at the
tip, sweeps back along the second arc and then turns 60 degrees right.
A whole petal leaves the turtle turned 230 degrees from where it
started, so the petals fan out in 36 directions 10 degrees apart, with
yellow and red taking turns around the flower.

The petals are drawn in 120 rounds of four, and the arc radius shrinks
by one pixel per round, from 200 down to 81, so each direction collects
a stack of 13 or 14 nested petals, each a little shorter than the one
before. Near the center the overlapping arcs merge into solid yellow
and red rays around a small black hole. The hole is there because the
90-degree turn at the tip is 10 degrees more than a petal needs to
close: each petal ends a short way from where it began, so the petals
start from a small ring around the center rather than from the center
itself.
"""

import turtle

PETAL_COLORS = ("yellow", "red", "yellow", "red")  # One round's petals.
ROUND_COUNT = 120
START_RADIUS = 200
ARC_EXTENT = 100


def draw_petal(pen, radius):
    """Draw one pointed petal from two arcs, then aim the next one."""
    pen.circle(radius, ARC_EXTENT)
    pen.left(90)
    pen.circle(radius, ARC_EXTENT)
    pen.right(60)  # Aims the next petal 230 degrees away from this one.


def draw_flower(pen):
    """Draw all the petals, shrinking the arcs after each round."""
    for round_number in range(ROUND_COUNT):
        for color in PETAL_COLORS:
            pen.color(color)
            draw_petal(pen, START_RADIUS - round_number)


def main():
    """Draw the flower and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Yellow and Red Flower")
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.hideturtle()
    draw_flower(pen)

    turtle.done()


if __name__ == "__main__":
    main()
