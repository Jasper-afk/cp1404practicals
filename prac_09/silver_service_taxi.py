"""
CP1404 Practical 9
Silver Service Taxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Template for SilverServiceTaxi objects."""

    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise an instance of the SilverServiceTaxi class."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like in the Taxi superclass but with the flagfall fee."""
        return f"{super().__str__()} plus flagfall of ${self.flag_fall:.2f}"

    def get_fare(self):
        """Return taxi fare as in Taxi superclass but with added flag fall fee."""
        return super().get_fare() + self.flag_fall
