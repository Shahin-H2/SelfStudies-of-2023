"""Rainbow mandala.

Draws a circular mandala of 180 motifs on a black background with a
2-pixel pen. Each motif is a rhombus with 100-pixel sides (two
equilateral triangles) pointing out from the center, with a circle of
radius 50 hanging off its outer tip. The motifs are drawn in pairs that
point in opposite directions: the first motif leaves the turtle turned
240 degrees, so its mirror image points the other way and undoes the
turn. The turtle turns 2 degrees after each pair, so 90 pairs place a
motif every 2 degrees all the way around. The overlapping rhombi form a
starburst that reaches 173 pixels from the center, and the overlapping
circles form a ring of loops around it that reaches 273 pixels.

Each motif has a single color, and the hue moves one fiftieth of the
way around the color wheel from one motif to the next, starting at red.
The two motifs of a pair land on opposite sides, so neighbors on the
circle are two steps apart in drawing order and the rainbow repeats
every 50 degrees around the circle. The colors jump at the two seams
where the first and last pairs meet, cutting two of the eight rainbows
short.
"""

import colorsys
import turtle

PAIR_COUNT = 90
PAIR_TURN = 2  # Pairs face both ways, so 180 degrees covers the circle.
SIDE_LENGTH = 100
LOOP_RADIUS = 50
HUE_STEP = 0.02


def draw_motif(pen, direction):
    """Draw a rhombus-and-loop motif, mirrored when direction is -1."""
    # Negative angles and radii turn the other way, mirroring the motif.
    pen.forward(SIDE_LENGTH)
    pen.left(60 * direction)
    pen.forward(SIDE_LENGTH)
    pen.right(120 * direction)
    pen.circle(LOOP_RADIUS * direction)
    pen.left(240 * direction)
    pen.forward(SIDE_LENGTH)
    pen.left(60 * direction)
    pen.forward(SIDE_LENGTH)


def draw_mandala(pen):
    """Draw the pairs of motifs, shifting the hue for every motif."""
    hue = 0.001
    for _ in range(PAIR_COUNT):
        for direction in (1, -1):
            pen.color(colorsys.hsv_to_rgb(hue, 1, 1))
            draw_motif(pen, direction)
            hue += HUE_STEP
        pen.left(PAIR_TURN)


def main():
    """Draw the mandala and keep the window open until it is closed."""
    screen = turtle.Screen()
    screen.title("Rainbow Mandala")
    screen.bgcolor("black")
    screen.tracer(5)  # Redraw only every 5th update, for speed.

    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.hideturtle()
    pen.width(2)
    draw_mandala(pen)

    turtle.done()


if __name__ == "__main__":
    main()
