"""
CP1404 Practical 9
Silver Service Taxi class test file
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run tests on the SilverServiceTaxi class."""
    fancy_taxi = SilverServiceTaxi("Limo", 200, 2)
    fancy_taxi.drive(18)
    bill = fancy_taxi.get_fare()
    assert bill == 48.80
    print(f"{bill:.2f}")


main()
