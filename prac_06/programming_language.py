"""CP1404 Practical 6 programming language class."""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """Initialise an instance of the programming language class."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if a language typing is dynamic or not."""
        return self.typing.title() == 'Dynamic'
