"""Car simulator: a tiny text-based command game.

Type commands at the ``>`` prompt to control an imaginary car:

    start - start the car
    stop  - stop the car
    help  - show the list of commands
    quit  - leave the game

The game remembers whether the car is running, so starting a car that
is already running (or stopping one that is already stopped) prints a
friendly warning. Commands are case-insensitive, and anything else is
answered with "Sorry, I don't understand that".
"""

HELP_TEXT = """
start - to start the car
stop - to stop the car
quit - to exit
"""


def main():
    """Read and run commands until the player types ``quit``."""
    print('Type "help" for more info...')
    started = False
    while True:
        command = input("> ").lower()
        if command == "start":
            if started:
                print("Hey! Car has already been started...")
            else:
                started = True
                print("Car started...ready to go.")
        elif command == "stop":
            if not started:
                print("Hey! Car has already been stopped...")
            else:
                started = False
                print("Car stopped.")
        elif command == "help":
            print(HELP_TEXT)
        elif command == "quit":
            print("Game Over")
            break
        else:
            print("Sorry, I don't understand that")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame Over")
