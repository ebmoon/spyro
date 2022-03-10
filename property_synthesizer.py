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
        self._infile = infile
        self._outfile = outfile
        
        # Temporary filename for iteration
        self._tempfile_name = get_tempfile_name(infile, outfile)
        
        # Template for Sketch synthesis
        self._template = infile.read()

        # Sketch Input File Generator
        self._input_generator = InputGenerator(self._template)

        # Initial list of positive/negative examples
        self._pos_examples = []
        self._neg_examples = []
        self._discarded_examples = []
        
        # Synthesized property
        self._phi = "out = false;"
        self._phi_conj = "out = true;"
        self._phi_list = []

        # Boolean variables for iteration
        self._is_sound = False
        self._is_precise = True

        # Options
        self._verbose = True
        self._check_soundness_first = True

        # Iterators for descriptive message
        self._inner_iterator = 0
        self._outer_iterator = 0

    def _write_output(self, output):
        self._outfile.write(output)

    def _get_new_tempfile_path(self):
        path = TEMP_FILE_PATH
        path += self._tempfile_name
        # path += f'_{self._outer_iterator}_{self._inner_iterator}'
        path += ".sk"

        self._inner_iterator += 1

        return path        

    def _try_synthesis(self, path):
        try:
            return subprocess.check_output([SKETCH_BINARY_PATH, path], stderr=subprocess.PIPE, timeout=120)
        except subprocess.CalledProcessError as e:
            return None
        except subprocess.TimeoutExpired as e:
            print("Timeout")
            return None

    def _run_synthesize(self):
        if self._verbose:
            print(f'Iteration {self._outer_iterator} - {self._inner_iterator}: Try synthesis')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_synthesis_input(self._phi, self._pos_examples, self._neg_examples)        

        write_tempfile(path, code)
        output = self._try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            return output_parser.parse_property()
        else:
            return None

    def _run_soundness_check(self):
        if self._verbose:
            print(f'Iteration {self._outer_iterator} - {self._inner_iterator}: Check soundenss')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_soundness_input(self._phi, self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = self._try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            pos_example = output_parser.parse_positive_example() 
            return (False, pos_example)
        else:
            return (True, None)

    def _run_precision_check(self):
        if self._verbose:
            print(f'Iteration {self._outer_iterator} - {self._inner_iterator}: Check precision')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_precision_input(
                self._phi, self._phi_list, self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = self._try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            neg_example = output_parser.parse_negative_example() 
            phi = output_parser.parse_property()
            return (False, neg_example, phi)
        else:
            return (True, None, None)

    def _run_max_sat(self):
        if self._verbose:
            print(f'Iteration {self._outer_iterator} - {self._inner_iterator}: Run MaxSat')

        path = TEMP_FILE_PATH + self._tempfile_name + ".sk"
        code = self._input_generator \
            .generate_maxsat_input(self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = self._try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            neg_examples, discarded_examples = output_parser.parse_maxsat(self._neg_examples) 
            phi = output_parser.parse_property()
            return (neg_examples, discarded_examples, phi)
        else:
            raise Error("MaxSat Failed")

    def _synthesizeProperty(self):
        is_sound = False
        is_precise = True

        while not is_sound or not is_precise:
            if not is_sound and not is_precise:
                phi = self._run_synthesize()
                if phi == None:
                    neg_examples, discarded_examples, phi = self._run_max_sat()
                    self._neg_examples = neg_examples
                    self._discarded_examples += discarded_examples
                    self._phi = phi
                else:
                    self._phi = phi

            if not is_sound:
                is_sound, e = self._run_soundness_check()
                if not is_sound:
                    is_precise = False
                    self._pos_examples.append(e)
            else:
                is_precise, e, phi = self._run_precision_check()
                if not is_precise:
                    is_sound = False
                    self._phi = phi
                    self._neg_examples.append(e)

    def _add_prop_to_conjunction(self):
        self._phi_conj += f'\n\tboolean prev_out_{self._outer_iterator} = out;'
        self._phi_conj += '\n\t'
        self._phi_conj += self._phi
        self._phi_conj += f'\n\tout = prev_out_{self._outer_iterator} && out;'

    def _check_change_behavior(self):
        if self._verbose:
            print(f'Iteration {self._outer_iterator} : Check termination')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_change_behavior_input(self._phi, self._phi_list)        
        
        write_tempfile(path, code)
        output = self._try_synthesis(path)

        return output != None

    def _synthesizeAllProperties(self):
        while True:
            self._synthesizeProperty()
            if not self._check_change_behavior():
                break

            self._phi_list.append(self._phi)
            self._add_prop_to_conjunction()
            self._neg_examples = []
            # self._neg_examples = self._discarded_examples
            # To-Do: Checks whether e \models phi_conj

            print("Obtained a best L-property")
            self._write_output(self._phi + '\n')

            self._outer_iterator += 1
            self._inner_iterator = 0
            self._phi = "out = false;"

    def run(self):
        self._synthesizeAllProperties()
        for i, phi in enumerate(self._phi_list):
            self._write_output(f'Output {i}\n')
            self._write_output(phi)
            self._write_output('\n')    