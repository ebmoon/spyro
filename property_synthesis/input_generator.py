import os
from util import *

OBTAINED_PROPERTY_HOLE = "OBTAINED_PROPERTY"

def split_function_from_code(code, function_name):
    lines = code.splitlines()

    target = 'harness void ' + function_name
    start = find_linenum_starts_with(lines, target)
    end = find_linenum_starts_with(lines, '}', start)

    remainder = '\n'.join(lines[:start] + lines[end + 1:])
    function = '\n'.join(lines[start:end+1])

    return (remainder, function)

class InputGenerator:

    def __init__(self, code):
        # Input code
        self._code = code

        # Split input code into three parts
        code, soundness_code = split_function_from_code(code, 'soundness')
        code, precision_code = split_function_from_code(code, 'precision')

        self._implenetation = code
        self._soundness_code = soundness_code
        self._precision_code = precision_code

        # The property obtained from the last synthesis
        self._obtained_property = "false"

    def set_obtained_property(self, obtained_property):
        self._obtained_property = obtained_property

    def _generate_common_part(self, positive_examples, negative_examples):
        # TO-DO: Add positive example part
        # TO-DO: Add negative example part

        code = self._implenetation.replace(
            "OBTAINED_PROPERTY", self._obtained_property)

        return code       

    def generate_soundness_input(self, positive_examples, negative_examples):
        # TO-DO: Implement

        code = self._generate_common_part(positive_examples, negative_examples)
        code += '\n'
        code += self._soundness_code

        return code

    def generate_precision_input(self, positive_examples, negative_examples):
        # TO-DO: Implement

        code = self._generate_common_part(positive_examples, negative_examples)
        code += '\n'
        code += self._precision_code

        return code

    def generate_maxsat_input(self, positive_examples, negative_examples):
        # TO-DO: Implement

        code = self._generate_common_part(positive_examples, negative_examples)

        return code