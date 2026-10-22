"""
Intended time:
Actual time:

"""

class ProgrammingLanguage:
    """Represent a programming language."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typinf, Reflection={self.reflection}, First appeared in {self.year}"