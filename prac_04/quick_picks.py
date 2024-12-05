"""CP1404 practical 4 quick picks program."""

from random import randint

AMOUNT_OF_NUMBERS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Print random quick pick numbers."""
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_picks = []
        for j in range(AMOUNT_OF_NUMBERS):
            number = randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_picks:
                number = randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()
