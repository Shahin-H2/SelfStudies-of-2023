print("""
Hey there, welcome to the Messenger of Love
To proceed, We will like to know what Status the Sender of this link asked you to input. See instructions below:
Type Single if you were asked to input Single
Type Relationship if you were asked to input Relationship
Type Crush if you were asked to input Crush
Type Forgive if you were asked to input Forgive
Type GoodEx if you were asked to input GoodEx
""")
command = ""
while True:
    command = input("What were you asked to input: ").lower()
    if command == "single":
        target_name = input("What is your name: ").upper()
        print(f"""
        Dear {target_name}
        
        The sad reality is that not everyone will be lucky to find the right one but here is wishing you find the right person that will bring so much joy and peace into your life and may your "Relationship" dreams come true.
        
        Hang in there!
        """)
        break
    elif command == "relationship":
        sender_name = input(
            "What is the name of the person who sent you this link: ").upper()
        target_name = input("What is your name: ").upper()
        print(f"""
        Dear {target_name}

        Everyday, I will choose you. No matter what life throws at us and how difficult things get, I will choose you. 
        I am grateful I have you in my life. Each day I love you more, today more than yesterday and less than tomorrow.
        Happy Valentine's day

        With love,
        {sender_name}
                """)
        break
    elif command == "crush":
        sender_name = input(
            "What is the name of the person who sent you this link: ").upper()
        target_name = input("What is your name: ").upper()
        print(f"""
        Dear {target_name}

        You have been in my dreams for a long time, what about making it real for once.
        I have a crush on you and I hope to be in a relationship with you someday.

        XOXO,
        {sender_name}
        """)
        break
    elif command == "forgive":
        sender_name = input(
            "What is the name of the person who sent you this link: ").upper()
        target_name = input("What is your name: ").upper()
        print(f"""
        Dear {target_name}

        I am an imperfect being, but this does not justify the mistakes that I have made to you. 
        I understand that even if I say sorry, it will not change anything. 
        However, I will keep my promise that I will change because I want to become a better person for you.

        With love,
        {sender_name}
        """)
        break
    elif command == "goodex":
        sender_name = input(
            "What is the name of the person who sent you this link: ").upper()
        target_name = input("What is your name: ").upper()
        print(f"""
        Dear {target_name}

        You are the best thing that has happened to me and I will choose you all over again.
        I cherish all the memories and the times we shared. Can we try one more time?

        With love,
        {sender_name}
        """)
        break
    else:
        print("Looks like you typed the wrong input")
        start_again = input("Do you want to start again? Yes or No: ").lower()
        if start_again == "no":
            print("Goodbye!")
            break
print("We hope you have a smile on your face")