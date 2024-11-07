"""CP1404 Practical 6 guitar class tests."""

from prac_06.guitar import Guitar


def run_tests():
    """Run tests on the Guitar class."""
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1.99)

    print(f"{gibson_guitar.name} get_age() - Expected 100. got {gibson_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. got {another_guitar.get_age()}")

    print(f"{gibson_guitar.name} is_vintage() - Expected True. got {gibson_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. got {another_guitar.is_vintage()}")


run_tests()
