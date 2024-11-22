"""
CP1404 Practical 9
UnreliableCar class
"""

from random import randint

from prac_09.car import Car


class UnreliableCar(Car):
    """Template for Unreliable Car objects."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise an instance of the UnreliableCar class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return string like parent Car class but with reliability percentage."""
        return f"{super().__str__()}, {self.reliability}% reliability"

    def drive(self, distance):
        """Drive like parent Car class but has a chance to fail."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return "failed to drive"
