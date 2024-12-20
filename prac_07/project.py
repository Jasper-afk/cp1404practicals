"""
CP1404 Practical 7 - Project class file.
"""

class Project:
    """Represent what will be in a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise an instance of the Project class."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return official string representation of a Project object."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${
        self.cost_estimate:.2f}, completion: {self.completion_percentage}%"