import os
from template_parser import TemplateParser
from util import *

class InputGenerator:
    # To-Do: Generate codes from variables and relations

    def __init__(self, code):
        # Input code
        self.__template = TemplateParser(code)

    def __soundness_code(self):
        code = 'harness void soundness() {\n'
        code += self.__template.get_variables_with_hole() + '\n\n'
        code += self.__template.get_relations() + '\n\n'
        
        code += '\tboolean out;\n'
        code += '\tobtained_property(' + self.__template.get_arguments_call() + ',out);\n'
        code += '\tassert !out;\n'
        
        code += '}\n\n'

        return code

    def __precision_code(self):
        code = 'harness void precision() {\n'
        code += self.__template.get_variables_with_hole() + '\n\n'
        
        arguments = self.__template.get_arguments_call()

        code += '\tboolean out_1;\n'
        code += '\tobtained_property(' + arguments + ',out_1);\n'
        code += '\tassert out_1;\n\n'

        code += '\tboolean out_2;\n'
        code += '\tproperty_conj(' + arguments + ',out_2);\n'
        code += '\tassert out_2;\n\n'

        code += '\tboolean out_3;\n'
        code += '\tproperty(' + arguments + ',out_3);\n'
        code += '\tassert !out_3;\n'
        code += '}\n\n'

        return code

    def __change_behavior_code(self):
        code = 'harness void change_behavior() {\n'
        code += self.__template.get_variables_with_hole() + '\n\n'
        
        arguments = self.__template.get_arguments_call()

        code += '\tboolean out_1;\n'
        code += '\tproperty_conj(' + arguments + ',out_1);\n'
        code += '\tassert out_1;\n\n'

        code += '\tboolean out_2;\n'
        code += '\tobtained_property(' + arguments + ',out_2);\n'
        code += '\tassert !out_2;\n'
        
        code += '}\n\n'

        return code

    def __property_code(self):
        code = 'void property('
        code += self.__template.get_arguments_defn()
        code += ',ref boolean out) {\n'
        code += '\tout = propertyGen(' + self.__template.get_arguments_call() + ');\n'
        code += '}\n\n'

        return code

    def __obtained_property_code(self, phi):
        code = 'void obtained_property('
        code += self.__template.get_arguments_defn()
        code += ',ref boolean out) {\n'
        code += '\t' + phi + '\n'
        code += '}\n\n'

        return code

    def __prev_property_code(self, i, phi):
        code = f'void prev_property_{i}('
        code += self.__template.get_arguments_defn()
        code += ',ref boolean out) {\n'
        code += '\t' + phi + '\n'
        code += '}\n\n'

        return code

    def __property_conj_code(self, phi_list):
        code = ''

        for i, phi in enumerate(phi_list):
            code += self.__prev_property_code(i, phi) + '\n\n'      

        code += 'void property_conj('
        code += self.__template.get_arguments_defn()
        code += ',ref boolean out) {\n'

        for i in range(len(phi_list)):
            code += f'\tboolean out_{i};\n'
            code += f'\tprev_property_{i}(' 
            code += self.__template.get_arguments_call() 
            code += f',out_{i});\n\n' 

        if len(phi_list) == 0:
            code += '\tout = true;\n'
        else:
            code += '\tout = ' + ' && '.join([f'out_{i}' for i in range(len(phi_list))]) + ';\n'
        code += '}\n\n'

        return code

    def __examples(self, pos_examples, neg_examples, check_maxsat = False):
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

    def __maxsat(self, num_neg_examples):
        code = 'harness void maxsat() {\n'
        code += f'\tint cnt = {num_neg_examples};\n'

        for i in range(num_neg_examples):
            code += f'\tif (??) {{ cnt -= 1; negative_example_{i}(); }}\n'

        code += '\tminimize(cnt);\n'
        code += '}\n\n'

        return code

    def __model_check(self, neg_example):
        code = 'harness void model_check() {\n'

        neg_example = '\n'.join(neg_example.splitlines()[:-1])
        code += neg_example.replace('property', 'property_conj')
        code += '\tassert out;\n'

        code += '\tboolean trivial_target = ??;\n'
        code += '\tassert trivial_target;\n'

        code += '}\n\n'

        return code

    def generate_synthesis_input(self, phi, pos_examples, neg_examples):
        code = self.__template.get_implementation()
        code += self.__examples(pos_examples, neg_examples)
        code += self.__property_code()

        return code

    def generate_soundness_input(self, phi, pos_examples, neg_examples):
        code = self.__template.get_implementation()
        code += self.__obtained_property_code(phi)
        code += self.__soundness_code()

        return code

    def generate_precision_input(self, phi, phi_list, pos_examples, neg_examples):
        code = self.__template.get_implementation()
        code += self.__examples(pos_examples, neg_examples)
        code += self.__property_code()
        code += self.__obtained_property_code(phi)
        code += self.__property_conj_code(phi_list)
        code += self.__precision_code()

        return code

    def generate_maxsat_input(self, pos_examples, neg_examples):
        code = self.__template.get_implementation()
        code += self.__examples(pos_examples, neg_examples, True)
        code += self.__property_code()
        code += self.__maxsat(len(neg_examples))

        return code

    def generate_change_behavior_input(self, phi, phi_list):
        code = self.__template.get_implementation()
        code += self.__property_conj_code(phi_list)
        code += self.__obtained_property_code(phi)
        code += self.__change_behavior_code()

        return code

    def generate_model_check_input(self, phi_list, neg_example):
        code = self.__template.get_implementation()
        code += self.__property_conj_code(phi_list)
        code += self.__model_check(neg_example)

        return code