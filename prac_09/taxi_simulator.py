"""
CP1404 Practical 9
Taxi Simulator exercise.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    """Taxi simulator program - choose a taxi, drive, gain bill."""

    total_bill = 0.0
    current_bill = 0.0
    current_taxi = None
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    print("Let's drive!")
    menu_choice = input(MENU).lower()
    while menu_choice != "q":

        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_taxi_choice(taxis)

        elif menu_choice == "d":
            if not current_taxi:  # Check if current_taxi is empty.
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi)
                current_bill = current_taxi.get_fare()
                total_bill += current_bill
                print(f"Your {current_taxi.name} trip cost you ${current_bill:.2f}")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        menu_choice = input(MENU).lower()

    print(f"Total trip cost: ${total_bill:.2f}\nTaxis are now:")
    display_taxis(taxis)


def drive_taxi(taxi):
    """Drive the current taxi."""
    taxi.start_fare()
    distance = get_valid_number("Drive how far? ")
    taxi.drive(distance)


def display_taxis(taxis):
    """Display a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_number(prompt=">>> ", error_message="Invalid number"):
    """Get a valid number."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(prompt))
            is_valid_input = True
        except ValueError:
            print(error_message)
    return number


def get_taxi_choice(taxis):
    """Get a taxi choice from the user, from a list of taxis."""
    taxi_choice = int(get_valid_number("Choose taxi: "))
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")


main()
