"""CP1404 practical 2 temperature conversion program."""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert Celsius to Fahrenheit and vice versa based on user input."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius and return the result."""
    return 5 / 9 * (fahrenheit - 32)


def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit and return the result."""
    return celsius * 9.0 / 5 + 32


main()
