"""CP1404 Practical 7 guitars exercise."""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


# TODO: Add docstring below.
def main():
    """..."""
    guitars = load_guitar_data(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitar_data(filename: str) -> list:
    """Load guitar data from a CSV file as Guitar objects in a list."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            parts[1] = int(parts[1])
            parts[2] = float(parts[2])
            guitars.append(Guitar(parts[0], parts[1], parts[2]))
        return guitars


main()
