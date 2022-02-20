import os

OBTAINED_PROPERTY_HOLE = "OBTAINED_PROPERTY"

class InputGenerator:

    def __init__(self, template):
        self._template = template
        self._obtained_property = "false"

    def set_obtained_property(self, obtained_property):
        self._obtained_property = obtained_property

    def generate_input(self, positive_examples, negative_examples):
        # TO-DO: Add positive example part
        # TO-DO: Add negative example part
        # TO-DO: Add max-sat part

        code = self._template.replace(
            "OBTAINED_PROPERTY", self._obtained_property)

        return code