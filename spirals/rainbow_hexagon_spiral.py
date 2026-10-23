"""Rainbow hexagon spiral.

Draws 360 straight lines on a black background. Each line is one pixel
longer than the one before it, and the turtle turns 59 degrees after
every line: one degree short of the 60 degrees that would close a
regular hexagon. That missing degree rotates every lap slightly, so the
hexagons twist into a spiral. The line colors cycle through red,
purple, blue, green, orange and yellow, and the pen grows one pixel
thicker every 100 lines, making the outer rings bolder than the center.
"""

import turtle

COLORS = ("red", "purple", "blue", "green", "orange", "yellow")
LINE_COUNT = 360
TURN_ANGLE = 59  # One degree short of a hexagon, so each lap rotates.


def draw_spiral(pen):
    """Draw the twisting hexagon spiral from the pen's position."""
    for step in range(LINE_COUNT):
        pen.pencolor(COLORS[step % len(COLORS)])
        pen.width(step // 100 + 1)
        pen.forward(step)
        pen.left(TURN_ANGLE)


def main():
    """Draw the spiral and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Rainbow Hexagon Spiral")
    screen.bgcolor("black")

    pen = turtle.Turtle()
    pen.speed("fastest")
    draw_spiral(pen)
    pen.hideturtle()

    turtle.done()


if __name__ == "__main__":
    main()
