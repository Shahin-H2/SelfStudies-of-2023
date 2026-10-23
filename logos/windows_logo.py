"""Windows logo.

Draws the flat, four-pane Windows logo (Windows 8/10 style) in bright
blue (#00adef) on a black background. The logo starts as one filled
four-sided shape in perspective: its left edge is 120 pixels tall and
its right edge 200 pixels tall, so it looks like a window seen at an
angle. Two 10-pixel lines in the background color then cut it into
four panes: a vertical one at x = 15 and a horizontal one at y = 0.
The vertical cut sits left of the shape's center, so the left panes
are narrower than the right ones. The turtle moves at speed 2, slowly
enough to watch each edge being drawn.
"""

import turtle

LOGO_COLOR = "#00adef"
BACKGROUND_COLOR = "black"
GAP_WIDTH = 10


def draw_logo_shape(pen):
    """Draw the blue logo as one filled four-sided shape."""
    pen.penup()
    pen.goto(-50, 60)
    pen.pendown()
    pen.color(LOGO_COLOR)
    pen.begin_fill()
    pen.goto(100, 100)
    pen.goto(100, -100)
    pen.goto(-50, -60)
    pen.goto(-50, 60)
    pen.end_fill()


def draw_gaps(pen):
    """Cut the logo into four panes with background-colored lines."""
    pen.color(BACKGROUND_COLOR)
    # Moving here with the pen down leaves a thin black line, visible
    # only as a small nick in the logo's top-left corner.
    pen.goto(15, 100)
    pen.width(GAP_WIDTH)
    pen.goto(15, -100)
    pen.penup()
    pen.goto(100, 0)
    pen.pendown()
    pen.goto(-100, 0)


def main():
    """Draw the logo and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Windows Logo")
    screen.bgcolor(BACKGROUND_COLOR)

    pen = turtle.Turtle()
    pen.speed(2)  # Slow on purpose, so you can watch it draw.
    draw_logo_shape(pen)
    draw_gaps(pen)

    turtle.done()


if __name__ == "__main__":
    main()
