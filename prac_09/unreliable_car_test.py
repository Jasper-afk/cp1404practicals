"""
CP1404 Practical 9
UnreliableCar class test file
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test a UnreliableCar object."""
    bad_car = UnreliableCar("Rust Bucket 9000", 100, 15)
    for i in range(100):
        print(bad_car.drive(50))


main()
