import subprocess
import os

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

    def _write_output(self, output):
        self._outfile.write(output)

    def _run_synthesizer_once(self, path):
        output = subprocess.check_output([SKETCH_BINARY_PATH, path])

        return output

    def run(self):
        # TO-DO: Iteration
        path = TEMP_FILE_PATH + self._tempfile_name + ".sk"
        code = self._input_generator.generate_soundness_input([], [])

        write_tempfile(path, code)
        output = self._run_synthesizer_once(path)
        
        output_parser = OutputParser(output)

        self._write_output(output)