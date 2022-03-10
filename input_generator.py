import os
from util import *

def split_section_from_code(code, section_name):
    target = section_name
    section_symbol_loc = code.find(target)
    start = code.find('{', section_symbol_loc)
    end = code.find('}', start)

    section_content = code[start+1:end]
    remainder = code[:section_symbol_loc] + code[end + 1:]

    return (remainder.strip(), section_content.strip())

def split_var_section(section_content):
    decls = [decl.strip().split() for decl in section_content.split(';')]
    return [(decl[0], decl[1]) for decl in decls[:-1]]

def split_relation_section(section_content):
    return [rel.strip() for rel in section_content.split(';')[:-1]]

class InputGenerator:
    # To-Do: Generate codes from variables and relations

    def __init__(self, code):
        # Input code
        self._code = code

        # Split input code into three parts
        code, variable_section = split_section_from_code(code, 'var')
        code, relation_section = split_section_from_code(code, 'relation')

        self._implenetation = code + '\n\n'
        self._var_decls = split_var_section(variable_section)
        self._relations = split_relation_section(relation_section)

    def _arguments_defn(self):
        return ','.join([typ + ' ' + symbol for typ, symbol in self._var_decls])

    def _arguments(self):
        return ','.join(symbol for _, symbol in self._var_decls)

    def _variables_hole(self):
        return '\n'.join(['\t' + typ + ' ' + symbol + ' = ??;' for typ, symbol in self._var_decls])

    def _relations_code(self):
        return '\n'.join(['\t' + rel + ';' for rel in self._relations])

    def _soundness_code(self):
        code = 'harness void soundness() {\n'
        code += self._variables_hole() + '\n\n'
        code += self._relations_code() + '\n\n'
        
        code += '\tboolean out;\n'
        code += '\tobtained_property(' + self._arguments() + ',out);\n'
        code += '\tassert !out;\n'
        
        code += '}\n\n'

        return code

    def _precision_code(self):
        code = 'harness void precision() {\n'
        code += self._variables_hole() + '\n\n'
        
        code += '\tboolean out_1;\n'
        code += '\tobtained_property(' + self._arguments() + ',out_1);\n'
        code += '\tassert out_1;\n\n'

        code += '\tboolean out_2;\n'
        code += '\tproperty_conj(' + self._arguments() + ',out_2);\n'
        code += '\tassert out_2;\n\n'

        code += '\tboolean out_3;\n'
        code += '\tproperty(' + self._arguments() + ',out_3);\n'
        code += '\tassert !out_3;\n'
        code += '}\n\n'

        return code

    def _change_behavior_code(self):
        code = 'harness void change_behavior() {\n'
        code += self._variables_hole() + '\n\n'
        
        code += '\tboolean out_1;\n'
        code += '\tproperty_conj(' + self._arguments() + ',out_1);\n'
        code += '\tassert out_1;\n\n'

        code += '\tboolean out_2;\n'
        code += '\tobtained_property(' + self._arguments() + ',out_2);\n'
        code += '\tassert !out_2;\n'
        
        code += '}\n\n'

        return code

    def _property_code(self):
        code = 'void property('
        code += self._arguments_defn()
        code += ',ref boolean out) {\n'
        code += '\tout = propertyGen(' + self._arguments() + ');\n'
        code += '}\n\n'

        return code

    def _obtained_property_code(self, phi):
        code = 'void obtained_property('
        code += self._arguments_defn()
        code += ',ref boolean out) {\n'
        code += '\t' + phi + '\n'
        code += '}\n\n'

        return code

    def _prev_property_code(self, i, phi):
        code = f'void prev_property_{i}('
        code += self._arguments_defn()
        code += ',ref boolean out) {\n'
        code += '\t' + phi + '\n'
        code += '}\n\n'

        return code

    def _property_conj_code(self, phi_list):
        code = ''

        for i, phi in enumerate(phi_list):
            code += self._prev_property_code(i, phi) + '\n\n'      

        code += 'void property_conj('
        code += self._arguments_defn()
        code += ',ref boolean out) {\n'

        for i in range(len(phi_list)):
            code += f'\tboolean out_{i};\n'
            code += f'\tprev_property_{i}(' + self._arguments() + f',out_{i});\n\n' 

        if len(phi_list) == 0:
            code += '\tout = true;\n'
        else:
            code += '\tout = ' + ' && '.join([f'out_{i}' for i in range(len(phi_list))]) + ';\n'
        code += '}\n\n'

        return code

    def _examples(self, pos_examples, neg_examples, check_maxsat = False):
        code = ''

        for i, pos_example in enumerate(pos_examples):
            code += '\n'
            code += 'harness void positive_example_{} ()'.format(i)
            code += ' {\n' + pos_example + '\n}\n\n'

        for i, neg_example in enumerate(neg_examples):
            code += '\n'
            if check_maxsat:
                code += 'void negative_example_{} ()'.format(i)
            else:   
                code += 'harness void negative_example_{} ()'.format(i)
            code += ' {\n' + neg_example + '\n}\n\n'      

        return code       

    def _maxsat(self, num_neg_examples):
        code = 'harness void maxsat() {\n'
        code += f'\tint cnt = {num_neg_examples};\n'

        for i in range(num_neg_examples):
            code += f'\tif (??) {{ cnt -= 1; negative_example_{i}(); }}\n'

        code += '\tminimize(cnt);\n'
        code += '}\n\n'

        return code

    def generate_synthesis_input(self, phi, pos_examples, neg_examples):
        code = self._implenetation
        code += self._examples(pos_examples, neg_examples)
        code += self._property_code()

        return code

    def generate_soundness_input(self, phi, pos_examples, neg_examples):
        code = self._implenetation
        code += self._obtained_property_code(phi)
        code += self._soundness_code()

        return code

    def generate_precision_input(self, phi, phi_list, pos_examples, neg_examples):
        code = self._implenetation
        code += self._examples(pos_examples, neg_examples)
        code += self._property_code()
        code += self._obtained_property_code(phi)
        code += self._property_conj_code(phi_list)
        code += self._precision_code()

        return code

    def generate_maxsat_input(self, pos_examples, neg_examples):
        code = self._implenetation
        code += self._examples(pos_examples, neg_examples, True)
        code += self._property_code()
        code += self._maxsat(len(neg_examples))

        return code

    def generate_change_behavior_input(self, phi, phi_list):
        code = self._implenetation
        code += self._property_conj_code(phi_list)
        code += self._obtained_property_code(phi)
        code += self._change_behavior_code()

        return code
