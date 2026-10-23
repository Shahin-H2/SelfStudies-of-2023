"""Black-and-white chessboard.

Draws an 8 x 8 chessboard of 30-pixel squares in a 600 x 600 window on
the default white background. The board starts at the center of the
window and extends 240 pixels up and to the right, so it sits in the
upper-right quarter. Rows are drawn from the bottom up, each one from
left to right. A square is black when its row and column numbers add
up to an even number and white otherwise, so the colors alternate along
every row and column and the bottom-left square is black. Every square
keeps the default thin black outline, which frames the white squares
against the white background.
"""

import turtle

SQUARES_PER_SIDE = 8
SQUARE_SIZE = 30
COLORS = ("black", "white")


def draw_square(pen, color):
    """Draw a filled square, then move to where the next one starts."""
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(SQUARE_SIZE)
        pen.left(90)
    pen.forward(SQUARE_SIZE)
    pen.end_fill()


def draw_board(pen):
    """Draw the board row by row, from the bottom row to the top."""
    for row in range(SQUARES_PER_SIDE):
        pen.penup()
        pen.goto(0, SQUARE_SIZE * row)
        pen.pendown()
        for column in range(SQUARES_PER_SIDE):
            draw_square(pen, COLORS[(row + column) % 2])


def main():
    """Draw the board and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Chessboard")
    screen.setup(600, 600)

    pen = turtle.Turtle()
    pen.speed("fastest")
    draw_board(pen)
    pen.hideturtle()

    turtle.done()


if __name__ == "__main__":
    main()
