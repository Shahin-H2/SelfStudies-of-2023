"""Tricolor triangle spiral.

Draws 300 straight lines on a black background. Each line is four
pixels longer than the one before it, and the turtle turns right 121
degrees after every line: one degree more than the 120 degrees that
would close an equilateral triangle. That extra degree leaves each
three-line lap three degrees clockwise of the one before, so the
growing triangles swirl outward. The lines cycle through white, pink
and cyan, which keeps each color on the same side of every triangle,
so the three colors sweep out three twisting arms.
"""

import turtle

COLORS = ("white", "pink", "cyan")
LINE_COUNT = 300
LENGTH_STEP = 4
TURN_ANGLE = 121  # One degree past a triangle, so each lap rotates.


def draw_spiral(pen):
    """Draw the three-armed triangle spiral from the pen's position."""
    for step in range(LINE_COUNT):
        pen.pencolor(COLORS[step % len(COLORS)])
        pen.forward(step * LENGTH_STEP)
        pen.right(TURN_ANGLE)


def main():
    """Draw the spiral and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Tricolor Triangle Spiral")
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.width(2)
    pen.speed("fastest")
    draw_spiral(pen)

    turtle.done()


if __name__ == "__main__":
    main()
