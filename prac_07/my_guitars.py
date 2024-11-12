"""CP1404 Practical 7 guitars exercise."""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Add new guitars to CSV file, formatted as (name, year, price), sorted by year."""
    guitars = load_guitars_data(FILENAME)
    guitars.sort()

    name = input("Name of guitar: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Price: "))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        print(f"{new_guitar} added to list.")
        name = input("Name of guitar: ")

    write_guitars_data(FILENAME, guitars)
    print(f"{len(guitars)} guitars added to {FILENAME}.")


def load_guitars_data(filename: str):
    """Load guitar data from a CSV file (name, year, price) as objects in a list."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            parts[1] = int(parts[1])
            parts[2] = float(parts[2])
            guitars.append(Guitar(parts[0], parts[1], parts[2]))
        return guitars


def write_guitars_data(filename: str, data: list):
    """Write Guitar list data to CSV file, formatted as (name, year, price)."""
    with open(filename, "w") as out_file:
        for record in data:
            print(f"{record.name},{record.year},{record.cost}", file=out_file)


main()
