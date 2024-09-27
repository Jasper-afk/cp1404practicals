"""CP1404 practical 2 score menu program."""

from score import determine_score

MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Print results category based on the score input."""
    score = int(get_valid_score())
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(get_valid_score())
        elif choice == "P":
            result = determine_score(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def print_stars(score: int) -> None:
    """Print stars multiplied by score."""
    print("*" * score, end="")
    print()


def get_valid_score() -> float:
    """Get a valid score."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
