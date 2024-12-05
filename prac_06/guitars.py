"""
CP1404 Practical 6 guitars exercise.
estimated: 40 minutes
actual: 52 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Program to add guitars to a list using the Guitar class."""
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        max_name_length = max(len(guitar.name) for guitar in guitars)
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {
            vintage_string}")
    else:
        print("No guitars.")


main()
