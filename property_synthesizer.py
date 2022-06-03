import subprocess
import os
import random
import time

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
    
    if infile_path != '<stdin>':
        return extract_filename_from_path(infile_path)
    
    return TEMP_NAME_DEFAULT

def write_tempfile(path, code):
    if not os.path.isdir(TEMP_FILE_PATH):
        os.mkdir(TEMP_FILE_PATH)

    with open(path, 'w') as f:
        f.write(code)

class PropertySynthesizer:
    def __init__(self, infile, outfile, verbose, inline_bnd, inline_bnd_sound, num_atom_max, enable_minimization) :       
        # Input/Output file stream
        self.__infile = infile
        self.__outfile = outfile
        
        # Temporary filename for iteration
        self.__tempfile_name = get_tempfile_name(infile, outfile)
        
        # Template for Sketch synthesis
        self.__template = infile.read()

        # Sketch Input File Generator
        self.__input_generator = InputGenerator(self.__template, enable_minimization)
        self.__input_generator.set_num_atom(num_atom_max)

        # Initial list of positive/negative examples
        self.__pos_examples = []
        self.__neg_examples = []
        self.__discarded_examples = []
        
        # Synthesized property
        self.__phi_initial = "out = false;"
        self.__phi_conj = "out = true;"
        self.__phi_list = []

        # Boolean variables for iteration
        self.__is_sound = False
        self.__is_precise = True

        # Options
        self.__verbose = verbose
        self.__check_soundness_first = True
        self.__enable_minimization = enable_minimization

        # Iterators for descriptive message
        self.__inner_iterator = 0
        self.__outer_iterator = 0

        self.__num_soundness = 0
        self.__num_precision = 0
        self.__num_maxsat = 0
        self.__num_synthesis = 0

        self.__time_soundness = 0
        self.__time_precision = 0
        self.__time_maxsat = 0
        self.__time_synthesis = 0

        self.__num_pos_examples = []
        self.__num_used_neg_examples = []
        self.__num_discarded_neg_examples = []

        self.__inline_bnd = inline_bnd
        self.__inline_bnd_sound = inline_bnd_sound

    def __write_output(self, output):
        self.__outfile.write(output)

    def __get_new_tempfile_path(self):
        path = TEMP_FILE_PATH
        path += self.__tempfile_name
        path += f'_{self.__outer_iterator}_{self.__inner_iterator}'
        path += ".sk"

        self.__inner_iterator += 1

        return path        

    def __try_synthesis(self, path, check_sound=False):
        inline_bnd = self.__inline_bnd if not check_sound else self.__inline_bnd_sound
        try:
            return subprocess.check_output( \
                [SKETCH_BINARY_PATH, path, '--bnd-inline-amnt', str(inline_bnd)], \
                stderr=subprocess.PIPE, timeout=300)
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

        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        end_time = time.time()

        self.__num_synthesis += 1
        self.__time_synthesis += end_time - start_time

        if output != None:
            output_parser = OutputParser(output)
            return output_parser.parse_property()
        else:
            return None

    def __run_soundness_check(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Check soundness')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_soundness_input(self.__phi, self.__pos_examples, self.__neg_examples)        
        
        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path, check_sound=True)

        end_time = time.time()

        self.__num_soundness += 1
        self.__time_soundness += end_time - start_time

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
        
        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        end_time = time.time()

        self.__num_precision += 1
        self.__time_precision += end_time - start_time

        if output != None:
            output_parser = OutputParser(output)
            pos_example = output_parser.parse_positive_example_precision() \
                if self.__enable_minimization else None
            neg_example = output_parser.parse_negative_example_precision() 
            phi = output_parser.parse_property()
            return (False, pos_example, neg_example, phi)
        else:
            return (True, None, None, None)

    def __run_max_sat(self):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Run MaxSat')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_maxsat_input(self.__pos_examples, self.__neg_examples)        
        
        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        end_time = time.time()

        self.__num_maxsat += 1
        self.__time_maxsat += end_time - start_time 

        if output != None:
            output_parser = OutputParser(output)
            neg_examples, discarded_examples = output_parser.parse_maxsat(self.__neg_examples) 
            phi = output_parser.parse_property()
            return (neg_examples, discarded_examples, phi)
        else:
            neg_examples = []
            discarded_examples = self.__neg_examples
            phi = 'out = true;'
            return (neg_examples, discarded_examples, phi)

    def __synthesizeProperty(self):
        self.__phi = self.__phi_initial
        is_sound = False
        is_precise = len(self.__pos_examples) == 0
        try_synthesis = True

        while not is_sound or not is_precise:
            if not is_sound and not is_precise and try_synthesis:
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
                try_synthesis = True
            else:
                is_precise, e_pos, e_neg, phi = self.__run_precision_check()
                if not is_precise:
                    is_sound = False
                    self.__phi = phi
                    self.__neg_examples.append(e_neg)
                    if e_pos != None:
                        self.__pos_examples.append(e_pos)
                    try_synthesis = False

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
            self.__num_pos_examples.append(len(self.__pos_examples))
            self.__num_used_neg_examples.append(len(self.__neg_examples))
            self.__num_discarded_neg_examples.append(len(self.__discarded_examples))

            self.__add_prop_to_conjunction()
            self.__neg_examples = [e for e in self.__discarded_examples if self.__model_check(e)]
            self.__discarded_examples = []

            if self.__verbose:
                print("Obtained a best L-property")
                print(self.__phi + '\n')

            self.__outer_iterator += 1
            self.__inner_iterator = 0

    def __statisticsList(self):
        statistics = []

        statistics.append(f'{self.__num_synthesis}')
        statistics.append(f'{self.__time_synthesis:.2f}s')
        statistics.append(f'{self.__num_maxsat}')
        statistics.append(f'{self.__time_maxsat:.2f}s')
        statistics.append(f'{self.__num_soundness}')
        statistics.append(f'{self.__time_soundness:.2f}s')
        statistics.append(f'{self.__num_precision}')
        statistics.append(f'{self.__time_precision:.2f}s')

        for i in range(len(self.__phi_list)):
            statistics.append(f'{self.__num_pos_examples[i]}')
            statistics.append(f'{self.__num_used_neg_examples[i]}')
            statistics.append(f'{self.__num_discarded_neg_examples[i]}')

        return statistics

    def __printStatistics(self):
        self.__write_output('-- Statistics --\n')

        self.__write_output(f'# synthesis: {self.__num_synthesis}\n')
        self.__write_output(f'Time spent on synthesis: {self.__time_synthesis:.2f}s\n\n')

        self.__write_output(f'# maxsat: {self.__num_maxsat}\n')
        self.__write_output(f'Time spent on maxsat: {self.__time_maxsat:.2f}s\n\n')

        self.__write_output(f'# soundness check: {self.__num_soundness}\n')
        self.__write_output(f'Time spent on soundness check: {self.__time_soundness:.2f}s\n\n')

        self.__write_output(f'# precision check: {self.__num_precision}\n')
        self.__write_output(f'Time spent on precision check: {self.__time_precision:.2f}s\n')

        self.__write_output('----------------\n')

        for i, phi in enumerate(self.__phi_list):
            self.__write_output(f'--- Output {i} ---\n')
            self.__write_output(phi)
            self.__write_output('\n')

            self.__write_output(f'# pos. examples: {self.__num_pos_examples[i]}\n')
            self.__write_output(f'# used neg. examples: {self.__num_used_neg_examples[i]}\n')
            self.__write_output(f'# discarded neg. examples: {self.__num_discarded_neg_examples[i]}\n')
            
            self.__write_output(f'----------------\n')

    def run(self):
        self.__synthesizeAllProperties()
        self.__printStatistics()


    def run_benchmark(self):
        self.__synthesizeAllProperties()
        statistics = self.__statisticsList()
        statistics = ','.join(statistics)

        self.__write_output(f'{statistics}\n')