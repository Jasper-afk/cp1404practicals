"""CP1404 Practical 6 guitar class."""

CURRENT_YEAR = 2022
VINTAGE_THRESHOLD = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise an instance of a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar object."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar object is vintage."""
        return self.get_age() >= VINTAGE_THRESHOLD
