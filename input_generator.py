import os
from util import *

def split_section_from_code(code, section_name):
    target = section_name
    section_symbol_loc = code.find(target)
    start = code.find('{', section_symbol_loc)
    end = code.find('}', start)

    section_content = code[start:end]
    remainder = code[:section_symbol_loc] + code[end + 1:]

    return (remainder, section_content)

def split_var_section(section_content):
    decls = [decl.strip().split() for decl in section_content.split(';')]
    return [(decl[0], decl[1]) for decl in decls]

def split_relation_section(section_content):
    return [rel.strip() for rel in section_content.split(';')]

class InputGenerator:
    # To-Do: Generate codes from variables and relations

    def __init__(self, code):
        # Input code
        self._code = code

        # Split input code into three parts
        code, variable_section = split_function_from_code(code, 'var')
        code, relation_section = split_function_from_code(code, 'relation')

        self._implenetation = code
        self._var_decls = split_var_section(variable_section)
        self._relations = split_relation_section(relation_section)

    def _arguments_defn(self):
        return ','.join([typ + ' ' + symbol for typ, symbol in self._var_decls])

    def _arguments(self):
        return ','.join(symbol for _, symbol in self._var_decls)

    def _variables_hole(self):
        return '\n'.join(['\t' + typ + ' ' + symbol '= ???;' for typ, symbol in self._var_decls])

    def _relations(self):
        return '\n'.join(['\t' + rel + ';' for rel in self._relations])

    def _soundness_code(self):
        code = 'harness void soundness('
        code += self._arguments_defn()
        code += ') {\n'
        code += self._variables_hole() + '\n\n'
        code += self._relations() + '\n\n'
        code += '\tboolean out;\n'
        code += '\tobtained_property(' + self._arguments() + ',out);\n'
        code += '\tassert !out;\n'
        code += '}'

        return code

    def _precision_code(self):
        # To-Do: Implement

        return ''

    def _add_behavior_code(self):
        # To-Do: Implement

        return ''

    def _property_code(self):
        # To-Do: Implement

        return ''

    def _obtained_property_code(self, phi):
        # To-Do: Implement

        return ''

    def _prev_property_code(self, n):
        # To-Do: Implement

        return ''

    def _property_conj_code(self, phi_list):
        # To-Do: Implement

        return ''

    def _examples(self, pos_examples, neg_examples, check_maxsat = False):
        code = ''

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
