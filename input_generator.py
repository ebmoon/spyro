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
        code, add_behavior_code = split_function_from_code(code, 'add_behavior')

        self._implenetation = code
        self._soundness_code = soundness_code
        self._precision_code = precision_code
        self._add_behavior_code = add_behavior_code

    def _generate_common_part(self, phi, phi_conj, pos_examples, neg_examples, check_maxsat = False):
        # TO-DO: Add positive example part
        # TO-DO: Add negative example part

        code = self._implenetation.replace('OBTAINED_PROPERTY', phi)
        code = code.replace('PROPERTY_CONJ', phi_conj)

        for i, pos_example in enumerate(pos_examples):
            code += '\n'
            code += 'harness void positive_example_{} ()'.format(i)
            code += ' {\n' + pos_example + '\n}\n'

        for i, neg_example in enumerate(neg_examples):
            code += '\n'
            if check_maxsat:
                code += 'void negative_example_{} ()'.format(i)
            else:   
                code += 'harness void negative_example_{} ()'.format(i)
            code += ' {\n' + neg_example + '\n}\n'      

        return code       

    def generate_synthesis_input(self, phi, phi_conj, pos_examples, neg_examples):
        code = self._generate_common_part(phi, phi_conj, pos_examples, neg_examples)

        return code

    def generate_soundness_input(self, phi, phi_conj, pos_examples, neg_examples):
        code = self._generate_common_part(phi, phi_conj, pos_examples, neg_examples)
        code += '\n'
        code += self._soundness_code

        return code

    def generate_precision_input(self, phi, phi_conj, pos_examples, neg_examples):
        code = self._generate_common_part(phi, phi_conj, pos_examples, neg_examples)
        code += '\n'
        code += self._precision_code

        return code

    def generate_maxsat_input(self, phi, phi_conj, pos_examples, neg_examples):
        num_neg_examples = len(neg_examples)

        code = self._generate_common_part(phi, phi_conj, pos_examples, neg_examples, True)
        code += '\nharness void maxsat() {'
        code += '\tint cnt = {};'.format(num_neg_examples)

        for i in range(num_neg_examples):
            code += '\n\tif (??) {{ cnt -= 1; negative_example_{}(); }}'.format(i)

        code += '\n\tminimize(cnt);'
        code += '\n}'

        return code

    def generate_add_behavior_input(self, phi_conj, phi):
        code = self._generate_common_part(phi, phi_conj, [], [])
        code += '\n'
        code += self._add_behavior_code

        return code
