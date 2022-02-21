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
    def __init__(self, infile, outfile):       
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
        
        # Synthesized property
        self._phi = "false"

        # Boolean variables for iteration
        self._is_sound = False
        self._is_precise = False

    def _write_output(self, output):
        self._outfile.write(output)

    def _run_synthesize(self):
        path = TEMP_FILE_PATH + self._tempfile_name + ".sk"
        code = self._input_generator
            .generate_synthesis_input(
                self._phi, self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = subprocess.check_output([SKETCH_BINARY_PATH, path])

        output_parser = OutputParser(output)
        if output_parser.check_sat:
            return output_parser.parse_property()
        else:
            return None

    def _run_soundness_check(self):
        path = TEMP_FILE_PATH + self._tempfile_name + ".sk"
        code = self._input_generator
            .generate_soundness_input(
                self._phi, self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = subprocess.check_output([SKETCH_BINARY_PATH, path])

        output_parser = OutputParser(output)
        if output_parser.check_sat:
            pos_example = output_parser.parse_positive_example() 
            return (False, pos_example)
        else:
            return (True, None)

    def _run_precision_check(self):
        path = TEMP_FILE_PATH + self._tempfile_name + ".sk"
        code = self._input_generator
            .generate_precision_input(
                self._phi, self._pos_examples, self._neg_examples)        
        
        write_tempfile(path, code)
        output = subprocess.check_output([SKETCH_BINARY_PATH, path])

        output_parser = OutputParser(output)
        if output_parser.check_sat:
            neg_example = output_parser.parse_negative_example() 
            phi = output_parser.parse_property()
            return (False, pos_example, phi)
        else:
            return (True, None, None)

    def _run_max_sat(self):
        # TO-DO: Impelment

        return ""

    def run(self):
        while not self._is_sound or not self._is_precise:
            if not self._is_sound and not self._is_precise:
                phi = self._run_synthesize()
                if phi == None:
                    self._run_max_sat()
                    # TO-DO: Update negative example
                    print ("Error: Not implemented")
                    break
                else:
                    self._phi = phi
                
            check_soundness = bool(random.getrandbits(1))
            if check_soundness:
                self._is_sound, e = self._run_soundness_check()
                if not self._is_sound:
                    self._is_precise = False
                    self._pos_examples.append(e)
            else:
                self._is_precise, e, phi = self._run_precision_check()
                if not self._is_precise:
                    self._is_sound = False
                    self._phi = phi
                    self._neg_examples.append(e)

        return self._phi