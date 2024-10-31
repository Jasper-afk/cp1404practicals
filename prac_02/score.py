"""CP1404 practical 2 determine score program."""

import random


def main():
    """Get score from the user and print the score category."""
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)
    result = determine_score(random.randint(1, 100))
    print(f"Random score: {result}")


def determine_score(score: float) -> str:
    """Determine the score category based on input."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Pass"
    return "Bad"


if __name__ == "__main__":
    main()
