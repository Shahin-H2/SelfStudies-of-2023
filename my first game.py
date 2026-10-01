print('Type "help" for more info...')
command = ""
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
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
        print("Game Over")
        break
    else:
        print("Sorry, I don't understand that")