"""Avengers logo.

Draws the Avengers "A" over a ring on a black background. The ring is
two filled circles that share a center: a red disc of radius 300 with
a 10-pixel white edge, then a black disc of radius 250 on top of it,
so only a red ring with a white outer edge stays visible.

The red "A" is drawn over the ring with the same white outline. It
has a slanted left leg, a flat top and a vertical right side, and its
top and left foot stick out past the ring. A black triangle with a
white edge forms the hole of the "A". Starting on the triangle's
right edge, two white strokes form a ">"-shaped arrowhead pointing
right.
"""

import turtle

LOGO_COLOR = "red"
OUTLINE_COLOR = "white"
BACKGROUND_COLOR = "black"
OUTLINE_WIDTH = 10


def draw_ring(pen):
    """Draw the red ring by covering a red disc with a black one."""
    pen.goto(0, -280)
    pen.pendown()
    pen.begin_fill()
    pen.color(LOGO_COLOR)
    pen.pencolor(OUTLINE_COLOR)
    pen.circle(300)
    pen.end_fill()
    pen.penup()

    # A black disc on the same center, (0, 20), leaves a red ring.
    pen.width(2)
    pen.goto(0, -230)
    pen.pendown()
    pen.begin_fill()
    pen.color(BACKGROUND_COLOR)
    pen.circle(250)
    pen.end_fill()
    pen.penup()


def draw_letter_a(pen):
    """Draw the red letter A with its thick white outline."""
    pen.goto(30, -110)
    pen.pendown()
    pen.begin_fill()
    pen.color(LOGO_COLOR)
    pen.width(OUTLINE_WIDTH)
    pen.pencolor(OUTLINE_COLOR)
    pen.forward(23)
    pen.backward(123)
    pen.left(60)
    pen.backward(220)
    pen.right(60)
    pen.backward(100)
    pen.right(117)
    pen.backward(710)
    pen.right(63)
    pen.backward(110)
    pen.right(90)
    pen.backward(510)
    pen.right(90)
    pen.backward(100)
    pen.right(90)
    pen.backward(70)
    pen.end_fill()
    pen.penup()


def draw_triangle_hole(pen):
    """Draw the black triangle that forms the hole of the letter A."""
    pen.goto(53, -40)
    pen.pendown()
    pen.begin_fill()
    pen.color(BACKGROUND_COLOR)
    pen.pencolor(OUTLINE_COLOR)
    pen.right(90)  # The letter A left the pen facing down; face left.
    pen.forward(100)
    pen.right(115)
    pen.forward(250)
    pen.right(157)
    pen.forward(227)
    pen.end_fill()
    # Leave the pen down: the arrowhead continues from here.


def draw_arrowhead(pen):
    """Draw the white arrowhead, starting where the triangle ends."""
    pen.backward(80)  # Back up the triangle's edge to start the arrow.
    pen.left(42)
    pen.forward(147)
    pen.right(83)
    pen.forward(140)


def main():
    """Draw the logo and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Avengers Logo")
    screen.bgcolor(BACKGROUND_COLOR)

    pen = turtle.Turtle()
    pen.speed("fast")
    pen.width(OUTLINE_WIDTH)
    pen.penup()
    # Order matters: each part starts from the prior part's pen state.
    draw_ring(pen)
    draw_letter_a(pen)
    draw_triangle_hole(pen)
    draw_arrowhead(pen)
    pen.hideturtle()

    turtle.done()


if __name__ == "__main__":
    main()
