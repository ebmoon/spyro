import subprocess
import os
import random

from input_generator import InputGenerator
from output_parser import OutputParser

SKETCH_BINARY_PATH = "sketch-frontend/sketch"
TEMP_FILE_PATH = "tmp/"
TEMP_NAME_DEFAULT = "tmp"

def extract_filename_from_path(path):
    basename = os.path.basename(path)
    filename, extension = os.path.splitext(basename)

    return filename

def get_tempfile_name(infile, outfile):
    infile_path = infile.name
    outfile_path = outfile.name

    if outfile_path != '<stdout>':
        return extract_filename_from_path(outfile_path)
    
    if infile_path != '<stdin>':
        return extract_filename_from_path(infile_path)
    
    return TEMP_NAME_DEFAULT

def write_tempfile(path, code):
    if not os.path.isdir(TEMP_FILE_PATH):
        os.mkdir(TEMP_FILE_PATH)

    with open(path, 'w') as f:
        f.write(code)

class PropertySynthesizer:
    def __init__(self, infile, outfile, verbose, soundness_first):       
        # Input/Output file stream
        self.__infile = infile
        self.__outfile = outfile
        
        # Temporary filename for iteration
        self.__tempfile_name = get_tempfile_name(infile, outfile)
        
        # Template for Sketch synthesis
        self.__template = infile.read()

        # Sketch Input File Generator
        self.__input_generator = InputGenerator(self.__template)

        # Initial list of positive/negative examples
        self.__pos_examples = []
        self.__neg_examples = []
        self.__discarded_examples = []
        
        # Synthesized property
        self.__phi = "out = false;"
        self.__phi_conj = "out = true;"
        self.__phi_list = []

        # Boolean variables for iteration
        self.__is_sound = False
        self.__is_precise = True

        # Options
        self.__verbose = True
        self.__check_soundness_first = True

        # Iterators for descriptive message
        self.__inner_iterator = 0
        self.__outer_iterator = 0

    def __write_output(self, output):
        self.__outfile.write(output)

    def __get_new_tempfile_path(self):
        path = TEMP_FILE_PATH
        path += self.__tempfile_name
        # path += f'_{self._outer_iterator}_{self._inner_iterator}'
        path += ".sk"

        self.__inner_iterator += 1

        return path        

    def __try_synthesis(self, path):
        try:
            return subprocess.check_output([SKETCH_BINARY_PATH, path], stderr=subprocess.PIPE, timeout=120)
        except subprocess.CalledProcessError as e:
            return None
        except subprocess.TimeoutExpired as e:
            print("Timeout")
            return None

    def __run_synthesize(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Try synthesis')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_synthesis_input(self.__phi, self.__pos_examples, self.__neg_examples)        

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            return output_parser.parse_property()
        else:
            return None

    def __run_soundness_check(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Check soundenss')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_soundness_input(self.__phi, self.__pos_examples, self.__neg_examples)        
        
        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            pos_example = output_parser.parse_positive_example() 
            return (False, pos_example)
        else:
            return (True, None)

    def __run_precision_check(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Check precision')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_precision_input(
                self.__phi, self.__phi_list, self.__pos_examples, self.__neg_examples)        
        
        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            neg_example = output_parser.parse_negative_example() 
            phi = output_parser.parse_property()
            return (False, neg_example, phi)
        else:
            return (True, None, None)

    def __run_max_sat(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Run MaxSat')

        path = TEMP_FILE_PATH + self.__tempfile_name + ".sk"
        code = self.__input_generator \
            .generate_maxsat_input(self.__pos_examples, self.__neg_examples)        
        
        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            neg_examples, discarded_examples = output_parser.parse_maxsat(self.__neg_examples) 
            phi = output_parser.parse_property()
            return (neg_examples, discarded_examples, phi)
        else:
            raise Exception("MaxSat Failed")

    def __synthesizeProperty(self):
        is_sound = False
        is_precise = True

        while not is_sound or not is_precise:
            if not is_sound and not is_precise:
                phi = self.__run_synthesize()
                if phi == None:
                    neg_examples, discarded_examples, phi = self.__run_max_sat()
                    self.__neg_examples = neg_examples
                    self.__discarded_examples += discarded_examples
                    self.__phi = phi
                else:
                    self.__phi = phi

            if not is_sound:
                is_sound, e = self.__run_soundness_check()
                if not is_sound:
                    is_precise = False
                    self.__pos_examples.append(e)
            else:
                is_precise, e, phi = self.__run_precision_check()
                if not is_precise:
                    is_sound = False
                    self.__phi = phi
                    self.__neg_examples.append(e)

    def __add_prop_to_conjunction(self):
        self.__phi_conj += f'\n\tboolean prev_out_{self.__outer_iterator} = out;'
        self.__phi_conj += '\n\t'
        self.__phi_conj += self.__phi
        self.__phi_conj += f'\n\tout = prev_out_{self.__outer_iterator} && out;'

    def __check_change_behavior(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} : Check termination')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_change_behavior_input(self.__phi, self.__phi_list)        
        
        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        return output != None

    def __model_check(self, neg_example):
        if self.__verbose:
            print(f'Iteratoin {self.__outer_iterator} : Model check')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_model_check_input(self.__phi_list, neg_example)

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        return output != None

    def __synthesizeAllProperties(self):
        while True:
            self.__synthesizeProperty()
            if not self.__check_change_behavior():
                break

            self.__phi_list.append(self.__phi)
            self.__add_prop_to_conjunction()
            self.__neg_examples = [e for e in self.__discarded_examples if self.__model_check(e)]
            self.__discarded_examples = []

            print("Obtained a best L-property")
            self.__write_output(self.__phi + '\n')

            self.__outer_iterator += 1
            self.__inner_iterator = 0
            self.__phi = "out = false;"

    def run(self):
        self.__synthesizeAllProperties()
        for i, phi in enumerate(self.__phi_list):
            self.__write_output(f'Output {i}\n')
            self.__write_output(phi)
            self.__write_output('\n')    