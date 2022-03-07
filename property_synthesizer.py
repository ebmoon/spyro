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

        # Number of sketch call
        self._iterator = 0


    def _write_output(self, output):
        self._outfile.write(output)

    def _get_new_tempfile_path(self):
        path = TEMP_FILE_PATH
        path += self._tempfile_name
        # path += '_{}'.format(self._iterator)
        path += ".sk"

        self._iterator += 1

        return path        

    def _try_synthesis(self, path):
        try:
            return subprocess.check_output([SKETCH_BINARY_PATH, path], stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            return None

    def _run_synthesize(self):
        if self._verbose:
            print(f'Iteration {self._iterator}: Try synthesis')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_synthesis_input(
                self._phi, self._pos_examples, self._neg_examples)        

        write_tempfile(path, code)
        output = self._try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            return output_parser.parse_property()
        else:
            return None

    def _run_soundness_check(self):
        if self._verbose:
            print(f'Iteration {self._iterator}: Check soundenss')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_soundness_input(
                self._phi, self._pos_examples, self._neg_examples)        
        
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
            print(f'Iteration {self._iterator}: Check precision')

        path = self._get_new_tempfile_path()
        code = self._input_generator \
            .generate_precision_input(
                self._phi, self._pos_examples, self._neg_examples)        
        
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
            print(f'Iteration {self._iterator}: Run MaxSat')

        path = TEMP_FILE_PATH + self._tempfile_name + ".sk"
        code = self._input_generator \
            .generate_maxsat_input(
                self._phi, self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = self._try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            neg_examples = output_parser.parse_maxsat(self._neg_examples) 
            return neg_examples
        else:
            raise Error("MaxSat Failed")

    def _synthesizeProperty(self):
        is_sound = False
        is_precise = True

        while not is_sound or not is_precise:
            if not is_sound and not is_precise:
                phi = self._run_synthesize()
                if phi == None:
                    self._neg_examples = self._run_max_sat()
                else:
                    self._phi = phi

            if is_sound:
                if is_sound:
                    continue

                is_sound, e = self._run_soundness_check()
                if not is_sound:
                    is_precise = False
                    self._pos_examples.append(e)
            else:
                if is_precise:
                    continue

                is_precise, e, phi = self._run_precision_check()
                if not is_precise:
                    is_sound = False
                    self._phi = phi
                    self._neg_examples.append(e)

    def _check_adds_behavior(self):
        # To-Do: Implement
        return True

    def _synthesizeAllProperties(self):
        # To-Do: Implement
        addsBehavior = False
        while not addsBehavior:
            self._synthesizeProperty()
            if self._check_adds_behavior():
                self._phi_list.append(self._phi)
                # To-Do: Implement conjunction
                # To-Do: Set initial set of negative examples

    def run(self):
        print("Obtained a best L-property")
        self._write_output(self._phi)