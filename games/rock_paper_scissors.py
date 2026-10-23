"""Rock, paper, scissors: a console game against the computer.

A welcome banner asks you to type ``start`` (or ``s``) to begin. Typing
``help`` (or ``h``) first explains that ``r``, ``p`` and ``s`` can be
used instead of rock, paper and scissors; any other answer prints
"something went wrong...." and ends the program. You then choose how
many points win the game, and the question is repeated until you enter
a whole number greater than 0. Answers are case-insensitive.

Every round the computer picks rock, paper or scissors at random, the
current score is shown and you type your move (``q`` or ``quit`` stops
the game early). The computer's move is revealed and the round goes to
the player, the computer or nobody (a tie): rock beats scissors,
scissors beat paper and paper beats rock. An unknown move is answered
with "something went wrong...." and the round starts over. At the end
the final score is printed above a banner naming whoever has more
points, or "IT'S A TIE!!" when you quit with the scores level.
"""

import random

MOVES = ("rock", "paper", "scissors")
ABBREVIATIONS = {"r": "rock", "p": "paper", "s": "scissors"}
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def wants_to_start():
    """Return True if the player asks to start, after optional help."""
    answer = input().lower()
    if answer in ("help", "h"):
        print("\nYou can use 'r', 'p', 's' instead of rock, paper, scissors\n")
        print("\nType 'start' or 's' to start the game...\n")
        answer = input().lower()
    return answer in ("start", "s")


def ask_points():
    """Return how many points win the game, asking until it is valid."""
    while True:
        answer = input("\nHow many points do you want to play? ")
        try:
            points = int(answer)
        except ValueError:
            points = 0  # Text is rejected just like zero or a negative.
        if points > 0:
            return points
        print("Please type a whole number greater than 0.")


def normalize_move(answer):
    """Return the full move name for an answer, or None if invalid."""
    move = ABBREVIATIONS.get(answer, answer)
    return move if move in MOVES else None


def format_scores(player_score, computer_score):
    """Return the scoreboard text shown every round and at the end."""
    return f"Player score = {player_score} | Computer score = {computer_score}"


def play_rounds(points_to_win):
    """Play rounds until a win or a quit; return the final scores."""
    player_score = 0
    computer_score = 0
    while player_score < points_to_win and computer_score < points_to_win:
        # The computer commits to its move before the player chooses.
        computer_move = random.choice(MOVES)
        print(f"\n{format_scores(player_score, computer_score)}")
        answer = input("Player, make your move: ").lower()
        if answer in ("q", "quit"):
            break

        print(f"Computer move is: {computer_move}")
        player_move = normalize_move(answer)
        if player_move is None:
            print("\n\t\tsomething went wrong....")
        elif player_move == computer_move:
            print("\nthat's a tie...\n")
        elif BEATS[player_move] == computer_move:
            print("\nPlayer wins...")
            player_score += 1
        else:
            print("\nComputer wins...")
            computer_score += 1
    return player_score, computer_score


def print_result(player_score, computer_score):
    """Print the final score and a banner for the winner or a tie."""
    print(f"\nFinal score: {format_scores(player_score, computer_score)}\n")
    if player_score > computer_score:
        print("\n\t\t\tPLAYER IS THE WINNER!!\n\n")
    elif computer_score > player_score:
        print("\n\t\t\tCOMPUTER IS THE WINNER!!\n\n")
    else:
        # Only reachable by quitting early with the scores level.
        print("\n\t\t\tIT'S A TIE!!\n\n")


def main():
    """Play one game of rock, paper, scissors against the computer."""
    print("\n\t\t\tWelcome to my game")
    print("\nType 'start' or 's' to start the game...")
    print("\nType 'help' for more information\n")

    if not wants_to_start():
        print("\n\t\tsomething went wrong....\n")
        return

    player_score, computer_score = play_rounds(ask_points())
    print_result(player_score, computer_score)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
