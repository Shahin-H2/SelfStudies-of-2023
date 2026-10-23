"""String permutations: a console program that prints every ordering.

Asks for a string and prints each permutation of its characters on its
own line, in the order ``itertools.permutations`` produces them. A
string of n characters gives n! lines, so the suggested input ``1234``
prints 24 lines, from ``1234`` to ``4321``. Characters are permuted by
position, not by value, so repeated characters give repeated lines:
``aab`` prints ``aab``, ``aba`` and ``baa`` twice each.
"""

from itertools import permutations


def print_permutations(text):
    """Print every permutation of ``text``, one per line."""
    for permutation in permutations(text):
        print("".join(permutation))


def main():
    """Ask for a string and print all of its permutations."""
    text = input("Enter your string (rec. 4 digits like 1234): ")
    print_permutations(text)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
