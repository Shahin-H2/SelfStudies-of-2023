# Python Turtle Graphics: Self-Study Portfolio

This repository collects small Python programs I wrote while teaching myself Python, starting in 2023. Most are generative art drawn with the standard-library `turtle` module, plus a few console programs. Nearly every script sits next to a screenshot of its output, so you can see what it does before running it.

<p align="center">
  <img src="patterns/rainbow_mandala.png" alt="Rainbow starburst inside a ring of overlapping loops on a black background" width="260">
  <img src="patterns/yellow_red_flower.png" alt="Dense flower of pointed yellow and red petals on a black background" width="260">
  <img src="logos/avengers_logo.png" alt="Red Avengers A with a white outline over a red ring on a black background" width="260">
</p>

## Contents

- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Gallery](#gallery)
  - [Logos](#logos)
  - [Patterns](#patterns)
  - [Spirals](#spirals)
- [Console programs](#console-programs)
  - [Basics](#basics)
  - [Games](#games)
- [What I practiced](#what-i-practiced)
- [Code style](#code-style)
- [License](#license)

## Repository structure

```text
Turtle-Lib-Practices-2023/
├── .gitignore
├── LICENSE
├── README.md
├── basics/     # Small console programs
│   ├── break_reminder.py
│   ├── love_messenger.png
│   ├── love_messenger.py
│   ├── string_permutations.png
│   └── string_permutations.py
├── games/      # Text-based console games
│   ├── car_simulator.png
│   ├── car_simulator.py
│   ├── rock_paper_scissors.png
│   └── rock_paper_scissors.py
├── logos/      # Turtle drawings: logo recreations
│   ├── avengers_logo.png
│   ├── avengers_logo.py
│   ├── windows_logo.png
│   └── windows_logo.py
├── patterns/   # Turtle drawings: geometric patterns
│   ├── chessboard.png
│   ├── chessboard.py
│   ├── rainbow_mandala.png
│   ├── rainbow_mandala.py
│   ├── yellow_red_flower.png
│   └── yellow_red_flower.py
├── requirements.txt
└── spirals/    # Turtle drawings: spirals from repeated turns
    ├── rainbow_hexagon_spiral.png
    ├── rainbow_hexagon_spiral.py
    ├── rainbow_hexagram.png
    ├── rainbow_hexagram.py
    ├── random_color_square_spiral.png
    ├── random_color_square_spiral.py
    ├── red_circle_vortex.png
    ├── red_circle_vortex.py
    ├── red_circle_vortex_fullscreen.png
    ├── tricolor_triangle_spiral.png
    └── tricolor_triangle_spiral.py
```

Each script and its screenshot share the same base name, such as `chessboard.py` and `chessboard.png`.

## Getting started

You need Python 3.8 or newer. The `turtle` module is part of the standard library but depends on Tkinter, which the python.org installers include. With Homebrew's Python, run `brew install python-tk`; on Debian or Ubuntu, run `sudo apt install python3-tk`.

```bash
git clone https://github.com/Shahin-H2/Turtle-Lib-Practices-2023.git
cd Turtle-Lib-Practices-2023
python3 spirals/rainbow_hexagon_spiral.py
```

Each turtle script opens a window and draws in it; closing the window ends the program. The **Run** commands below assume you are in the repository root. On Windows, use `py` in place of `python3`.

Only `basics/break_reminder.py` needs a third-party package, plyer:

```bash
pip install -r requirements.txt
```

On macOS, plyer also needs pyobjus (`pip install pyobjus`).

## Gallery

Turtle drawings, grouped by folder. Each preview is a screenshot of the finished drawing.

### Logos

Two well-known logos rebuilt by layering filled shapes and painting over parts of them in the background color.

| Preview | Script |
| :---: | :--- |
| <img src="logos/avengers_logo.png" alt="Red Avengers A with a white outline over a red ring on a black background" width="300"> | **[Avengers Logo](logos/avengers_logo.py)**<br>The red Avengers "A" with a thick white outline, laid over a red ring on a black background. The ring is a red disc with a smaller black disc painted over its middle; a black triangle cuts the hole in the "A", and two white strokes add the arrowhead.<br><br>**Concepts:** filled shapes, layering in the background color, separate outline and fill colors, helper functions<br>**Run:** `python3 logos/avengers_logo.py` |
| <img src="logos/windows_logo.png" alt="Blue four-pane Windows logo in perspective on a black background" width="300"> | **[Windows Logo](logos/windows_logo.py)**<br>The flat four-pane Windows logo in bright blue (`#00adef`) on a black background. It starts as one filled shape whose right edge is taller than its left, so it looks like a window seen at an angle, and two 10-pixel lines in the background color cut it into four panes. The turtle draws at speed 2, slow enough to watch each edge appear.<br><br>**Concepts:** filled polygons with `goto()`, drawing in the background color, pen width, animation speed<br>**Run:** `python3 logos/windows_logo.py` |

*Fan-made recreations for learning; the logos are trademarks of their respective owners.*

### Patterns

Repeating figures: a chessboard built square by square and two radial designs made from hundreds of overlapping shapes.

| Preview | Script |
| :---: | :--- |
| <img src="patterns/chessboard.png" alt="Black-and-white 8 by 8 chessboard in the upper-right quarter of a white window" width="300"> | **[Chessboard](patterns/chessboard.py)**<br>An 8 x 8 board of 30-pixel squares in the upper-right quarter of a 600 x 600 window, drawn row by row from the bottom. A square is black when its row and column numbers add up to an even number and white otherwise, and a thin black outline frames the white squares against the white background.<br><br>**Concepts:** nested loops, modular arithmetic, filled squares, functions with parameters<br>**Run:** `python3 patterns/chessboard.py` |
| <img src="patterns/rainbow_mandala.png" alt="Rainbow starburst inside a ring of overlapping loops on a black background" width="300"> | **[Rainbow Mandala](patterns/rainbow_mandala.py)**<br>A circle of 180 motifs, one every 2 degrees, that overlap into a rainbow starburst ringed by loops on a black background. Each motif is a rhombus pointing out from the center with a circle hanging off its tip, drawn in pairs that point in opposite directions; the hue shifts one fiftieth of the color wheel per motif, so the rainbow repeats every 50 degrees around the circle.<br><br>**Concepts:** HSV colors with `colorsys`, nested loops, a `direction` parameter that mirrors a shape, `tracer()` for faster drawing<br>**Run:** `python3 patterns/rainbow_mandala.py` |
| <img src="patterns/yellow_red_flower.png" alt="Dense flower of pointed yellow and red petals around a small black center" width="300"> | **[Yellow and Red Flower](patterns/yellow_red_flower.py)**<br>A dense flower of 480 pointed petals, alternating yellow and red, that fan out in 36 directions on a black background. Each petal is two 100-degree arcs that meet at a tip, and the arc radius shrinks by one pixel every round of four petals, so each direction collects a stack of nested petals. Near the center they merge into solid rays around a small black hole, left open because each petal ends a short way from where it began.<br><br>**Concepts:** arcs with `circle(radius, extent)`, nested loops, color cycling, angle arithmetic<br>**Run:** `python3 patterns/yellow_red_flower.py` |

### Spirals

Each spiral repeats one move many times, changing a length or a radius a little on every step and turning by a fixed angle.

| Preview | Script |
| :---: | :--- |
| <img src="spirals/rainbow_hexagon_spiral.png" alt="Twisting spiral of rainbow-colored hexagons with thicker outer lines on a black background" width="300"> | **[Rainbow Hexagon Spiral](spirals/rainbow_hexagon_spiral.py)**<br>Growing hexagons on a black background: 360 lines, each one pixel longer than the last, cycling through red, purple, blue, green, orange and yellow. The turtle turns 59 degrees after every line, one degree short of a hexagon, so each lap rotates slightly and the hexagons twist into a spiral; the pen also gets one pixel thicker every 100 lines, making the outer rings bolder.<br><br>**Concepts:** loops, modular arithmetic for color cycling, integer division for pen width, near-miss turning angles<br>**Run:** `python3 spirals/rainbow_hexagon_spiral.py` |
| <img src="spirals/rainbow_hexagram.png" alt="Six-pointed star of nested triangles shading from red to purple on a black background" width="300"> | **[Rainbow Hexagram](spirals/rainbow_hexagram.py)**<br>A six-pointed star on a black background, drawn from 80 lines with a 120-degree turn after each and every line 10 pixels shorter than the one before. The first 40 lines wind inward as triangles pointing up; the length then passes zero and turns negative, so the turtle walks backwards and the last 40 lines grow back out as triangles pointing down that interlock with the first set. The hue shifts a little with every line, from red through yellow and green to blue and purple.<br><br>**Concepts:** HSV colors with `colorsys`, negative distances, variables updated in a loop<br>**Run:** `python3 spirals/rainbow_hexagram.py` |
| <img src="spirals/random_color_square_spiral.png" alt="Web of twisted squares in random colors around a small black square" width="300"> | **[Random Color Square Spiral](spirals/random_color_square_spiral.py)**<br>Growing squares on a black background: 449 lines from 51 to 499 pixels long, each in its own random RGB color, so every run looks different. The turtle turns right 90.991 degrees after each line, just under one degree more than a square needs, so each lap of four lines lands almost four degrees clockwise of the last and the squares twist into a round web around a small black square.<br><br>**Concepts:** the `random` module, RGB colors with `colormode(255)`, functions that return a tuple, `range()` with a start and a stop<br>**Run:** `python3 spirals/random_color_square_spiral.py` |
| <img src="spirals/red_circle_vortex.png" alt="Red tunnel of overlapping circles around a round black hole" width="300"> | **[Red Circle Vortex](spirals/red_circle_vortex.py)**<br>Pairs of red circles on a black background: at each of 500 steps the turtle draws a circle whose radius equals the step number and a second one three quarters that size, both touching at its position. Between pairs it turns right 3 degrees and moves 3 pixels, walking just over four laps around a small circle; every circle touches that path from the outside, so they pile up into a red tunnel around a round black hole. See also the [full-screen screenshot](spirals/red_circle_vortex_fullscreen.png).<br><br>**Concepts:** `circle()` with growing radii, the loop variable as a size, small repeated turns<br>**Run:** `python3 spirals/red_circle_vortex.py` |
| <img src="spirals/tricolor_triangle_spiral.png" alt="Swirling triangle spiral with white, pink and cyan arms on a black background" width="300"> | **[Tricolor Triangle Spiral](spirals/tricolor_triangle_spiral.py)**<br>Growing triangles on a black background: 300 lines, each 4 pixels longer than the last, cycling through white, pink and cyan. The turtle turns right 121 degrees after every line, one degree past a triangle, so each lap lands three degrees clockwise of the one before and the triangles swirl outward; each color stays on the same side of every triangle, so the colors sweep out three twisting arms.<br><br>**Concepts:** modular arithmetic for color cycling, near-miss turning angles, pen width<br>**Run:** `python3 spirals/tricolor_triangle_spiral.py` |

## Console programs

These programs run in the terminal instead of a turtle window, and their screenshots are terminal captures.

### Basics

Short console programs built around input, text and the standard library, plus one that uses a third-party package.

| Preview | Script |
| :---: | :--- |
| *No screenshot: shows a desktop notification* | **[Break Reminder](basics/break_reminder.py)**<br>Shows a desktop notification, "Take a break! It has been an hour!", as soon as it starts and then once an hour until you press Ctrl+C. It needs the third-party plyer package (plus pyobjus on macOS) and prints an install hint if plyer is missing.<br><br>**Concepts:** third-party packages, an endless loop with `time.sleep()`, handling `ImportError` and `KeyboardInterrupt`<br>**Run:** `python3 basics/break_reminder.py` |
| <img src="basics/love_messenger.png" alt="Terminal session: the Single status prints a letter to SHAHIN that ends with Hang in there!" width="300"> | **[Love Messenger](basics/love_messenger.py)**<br>A personal letter generator: the reader types the status the sender asked for (Single, Relationship, Crush, Forgive or GoodEx) and the names the letter needs, then the program prints the matching letter with the names in capital letters. The status is case-insensitive, and an unknown one offers to start again.<br><br>**Concepts:** `input()`, string methods, dictionaries, `str.format()` templates, `textwrap.indent()`<br>**Run:** `python3 basics/love_messenger.py` |
| <img src="basics/string_permutations.png" alt="Terminal session: the input 1234 printed as all 24 permutations, from 1234 to 4321" width="300"> | **[String Permutations](basics/string_permutations.py)**<br>Asks for a string and prints every ordering of its characters, one per line, using `itertools.permutations`. A string of n characters gives n! lines, so the suggested input `1234` prints 24; characters are permuted by position, so repeated characters give repeated lines.<br><br>**Concepts:** `itertools.permutations`, `str.join()`, factorial growth<br>**Run:** `python3 basics/string_permutations.py` |

### Games

Two text-based games that loop on player input and keep track of state between turns.

| Preview | Script |
| :---: | :--- |
| <img src="games/car_simulator.png" alt="Terminal session: help, start, stop, two unknown commands and quit" width="300"> | **[Car Simulator](games/car_simulator.py)**<br>A tiny command game: type `start`, `stop`, `help` or `quit` (in any case) at the `>` prompt to control an imaginary car. The game remembers whether the car is running, so starting it twice or stopping it twice prints a warning, and any other command gets "Sorry, I don't understand that".<br><br>**Concepts:** `while` loops, `if`/`elif` chains, a Boolean state flag, case-insensitive input<br>**Run:** `python3 games/car_simulator.py` |
| <img src="games/rock_paper_scissors.png" alt="Terminal session: a one-point game that the player wins with rock against scissors" width="300"> | **[Rock, Paper, Scissors](games/rock_paper_scissors.py)**<br>A game against the computer: you choose how many points win, and the question repeats until you enter a whole number greater than 0. Each round the computer picks a random move and you type yours in full or as `r`, `p` or `s`; `q` quits early. A final banner names whoever has more points, or a tie when the scores are level.<br><br>**Concepts:** the `random` module, dictionaries as lookup tables, input validation with `try`/`except`, functions that return tuples, f-strings<br>**Run:** `python3 games/rock_paper_scissors.py` |

## What I practiced

- **Loops and modular arithmetic:** cycling through a color tuple with `step % len(COLORS)` and alternating squares with `(row + column) % 2` ([Rainbow Hexagon Spiral](spirals/rainbow_hexagon_spiral.py), [Chessboard](patterns/chessboard.py)).
- **HSV colors:** stepping the hue with `colorsys.hsv_to_rgb` for smooth rainbows ([Rainbow Mandala](patterns/rainbow_mandala.py), [Rainbow Hexagram](spirals/rainbow_hexagram.py)).
- **Randomness:** random RGB colors with `random.randint` and a random computer move with `random.choice` ([Random Color Square Spiral](spirals/random_color_square_spiral.py), [Rock, Paper, Scissors](games/rock_paper_scissors.py)).
- **Angles and geometry:** a turn one degree past a triangle that makes each lap rotate, a 230-degree net turn that spreads petals over 36 directions, and negative lengths that walk the turtle backwards ([Tricolor Triangle Spiral](spirals/tricolor_triangle_spiral.py), [Yellow and Red Flower](patterns/yellow_red_flower.py), [Rainbow Hexagram](spirals/rainbow_hexagram.py)).
- **Filled shapes and layering:** `begin_fill()` and `end_fill()`, plus painting in the background color to cut rings, holes and gaps ([Avengers Logo](logos/avengers_logo.py), [Windows Logo](logos/windows_logo.py)).
- **Functions with parameters:** small drawing helpers that take the pen and a color, radius or direction ([Chessboard](patterns/chessboard.py), [Yellow and Red Flower](patterns/yellow_red_flower.py), [Rainbow Mandala](patterns/rainbow_mandala.py)).
- **Input handling:** case-insensitive commands, asking again until the input is valid, and exiting cleanly on Ctrl+C ([Car Simulator](games/car_simulator.py), [Rock, Paper, Scissors](games/rock_paper_scissors.py), [Love Messenger](basics/love_messenger.py)).
- **Standard library and packages:** `itertools.permutations`, `textwrap.indent()` and a third-party package installed from `requirements.txt` ([String Permutations](basics/string_permutations.py), [Love Messenger](basics/love_messenger.py), [Break Reminder](basics/break_reminder.py)).

## Code style

The scripts follow PEP 8 and PEP 257: each one opens with a module docstring that describes its output and has a `main()` function that runs under an `if __name__ == "__main__":` guard. Turtle scripts end with `turtle.done()`, so the window stays open until you close it, and console programs exit cleanly on Ctrl+C with a short message instead of a traceback.

## License

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for the full text.
