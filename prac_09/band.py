"""
CP1404 Practical 9
Band class
"""


class Band:
    """Template for a Band class instance."""

    def __init__(self, name):
        """Initialise instance of the Band class and its data."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def play(self):
        """Return a string of each member playing their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)

    def add(self, musician):
        """Add a musician to a band's list of members."""
        self.musicians.append(musician)
