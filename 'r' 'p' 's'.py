import random


# randomNumber = random.randint(0, 2)
# if randomNumber == 0:
#     computerMove = "rock"
# elif randomNumber == 1:
#     computerMove = "paper"
# elif randomNumber == 2:
#     computerMove = "scissors"

playerScore = 0
computerScore = 0
# winsScore

print("\n\t\t\tWelcom to my game")
print("\nType 'start' or 's' to start the game...")
print("\nType 'help' for more information\n")

start = input().lower()

if start == "help" or start == "h":
    print("\nYou can use 'r','p','s' insted of rock,paper,scissors\n")
    print("\nType 'start' or 's' to start the game...\n")
    start = input().lower()

if start == "start" or start == "s":
    winsScore = input("\nHow many points you want to play? ")
    winsScore = int(winsScore)
elif start != "start" or start != "s":
    print("\n\t\tsomething went wrong ....\n")
# else:
#     print("Good bye!")

while playerScore < winsScore and computerScore < winsScore:

    randomNumber = random.randint(0, 2)
    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

    print(f"\nPlayer score = {playerScore} | Computer score = {computerScore}")
    player = input("player , Make your move : ").lower()

    if player == "q" or player == "quit":
        break

    print(f"Computer move is : {computerMove}")

    if player == computerMove:
        print("\nthats a tie...\n")
    elif player == "rock" or player == "r":
        if computerMove == "paper" or computerMove == "p":
            print("\nComputer wins...")
            computerScore += 1
        elif computerMove == "scissors" or computerMove == "s":
            print("\nPlayer wins...")
            playerScore += 1
    elif player == "paper" or player == "p":
        if computerMove == "scissors" or computerMove == "s":
            print("\nComputer wins...")
            computerScore += 1
        elif computerMove == "rock" or computerMove == "r":
            print("\nPlayer wins...")
            playerScore += 1
    elif player == "scissors" or player == "s":
        if computerMove == "rock" or computerMove == "r":
            print("\nComputer wins...")
            computerScore += 1
        elif computerMove == "paper" or computerMove == "p":
            print("\nPlayer wins...")
            playerScore += 1
    else:
        print("\n\t\tsomething went wrong ....")

print(
    f"\nFinal score : Player score = {playerScore} | Computer score = {computerScore}\n")

if playerScore == winsScore:
    print("\n\t\t\tPLAYER IS THE WINNER!!\n\n")
else:
    print("\n\t\t\tCOMPUTER IS THE WINNER!!\n\n")