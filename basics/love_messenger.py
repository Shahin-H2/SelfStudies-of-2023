"""Messenger of Love: a console program that prints a personal letter.

The program greets the reader, lists the five statuses the sender of
the link may have chosen (Single, Relationship, Crush, Forgive and
GoodEx) and asks which one the reader was told to type; the answer is
case-insensitive. Every status except Single then asks for the sender's
name, and all of them ask for the reader's name. It prints the matching
letter, indented by eight spaces and opening with "Dear <READER>". The
Single letter ends with "Hang in there!"; the other four are signed
"With love," or "XOXO," above the sender's name. Names are printed in
capital letters.

Any other answer prints "Looks like you typed the wrong input" and asks
whether to start again: answering ``no`` prints "Goodbye!", anything
else asks for the status again. After the letter or that goodbye, the
program prints "We hope you have a smile on your face".
"""

import textwrap

# A trailing backslash keeps a long sentence on one printed line.
WELCOME = """
Hey there, welcome to the Messenger of Love
To proceed, we would like to know what Status the Sender of this link \
asked you to input. See instructions below:
Type Single if you were asked to input Single
Type Relationship if you were asked to input Relationship
Type Crush if you were asked to input Crush
Type Forgive if you were asked to input Forgive
Type GoodEx if you were asked to input GoodEx
"""
LETTER_INDENT = " " * 8

# print_letter() fills in {reader} and {sender} with str.format(), so
# a literal brace in a letter must be doubled.
SINGLE_LETTER = """
Dear {reader}

The sad reality is that not everyone will be lucky to find the right one
but here is wishing you find the right person that will bring so much \
joy and peace into your life
and may your "Relationship" dreams come true.

Hang in there!
"""

RELATIONSHIP_LETTER = """
Dear {reader}

Every day, I will choose you. No matter what life throws at us and how \
difficult things get, I will choose you.
I am grateful I have you in my life. Each day I love you more, today \
more than yesterday and less than tomorrow.
Happy Valentine's Day

With love,
{sender}
"""

CRUSH_LETTER = """
Dear {reader}

You have been in my dreams for a long time, what about making it real for once?
I have a crush on you and I hope to be in a relationship with you someday.

XOXO,
{sender}
"""

FORGIVE_LETTER = """
Dear {reader}

I am an imperfect being, but this does not justify the mistakes that I \
have made to you.
I understand that even if I say sorry, it will not change anything.
However, I will keep my promise that I will change because I want to \
become a better person for you.

With love,
{sender}
"""

GOODEX_LETTER = """
Dear {reader}

You are the best thing that has happened to me and I will choose you \
all over again.
I cherish all the memories and the times we shared. Can we try one more time?

With love,
{sender}
"""

LETTERS = {
    "single": SINGLE_LETTER,
    "relationship": RELATIONSHIP_LETTER,
    "crush": CRUSH_LETTER,
    "forgive": FORGIVE_LETTER,
    "goodex": GOODEX_LETTER,
}


def print_letter(status):
    """Ask for the names the letter needs, then print the letter."""
    sender_name = ""
    if status != "single":  # The Single letter is not signed.
        sender_name = input(
            "What is the name of the person who sent you this link: "
        ).upper()
    reader_name = input("What is your name: ").upper()
    template = textwrap.indent(LETTERS[status], LETTER_INDENT)
    print(template.format(sender=sender_name, reader=reader_name))


def main():
    """Ask for the status and print its letter, or say goodbye."""
    print(WELCOME)
    while True:
        status = input("What were you asked to input: ").lower()
        if status in LETTERS:
            print_letter(status)
            break
        print("Looks like you typed the wrong input")
        start_again = input("Do you want to start again? Yes or No: ").lower()
        if start_again == "no":
            print("Goodbye!")
            break
    print("We hope you have a smile on your face")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
