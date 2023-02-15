"""A data model for the Critical Success Factors of a project."""

class CSF:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other.name
