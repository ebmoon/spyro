import argparse
import subprocess
import sys
import os

SKETCH_BINARY_PATH = "sketch-frontend/sketch"
TEMP_FILE_PATH = "tmp/"
TEMP_NAME_DEFAULT = "tmp"

def extract_filename_from_path(path):
    basename = os.path.basename(path)
    filename, extension = os.path.splitext(basename)

    return filename

def temp_filename(infile, outfile):
    infile_path = infile.name
    outfile_path = outfile.name

    if outfile_path != '<stdout>':
        return extract_filename_from_path(outfile_path)
    
    if infile_path != '<stdin>':
        return extract_filename_from_path(infile_path)
    
    return TEMP_NAME_DEFAULT

def write_temp_file(infile, outfile):
    if not os.path.isdir(TEMP_FILE_PATH):
        os.mkdir(TEMP_FILE_PATH)

    filename = temp_filename(infile, outfile)
    path = TEMP_FILE_PATH + filename + ".sk"

    with open(path, 'w') as f:
        content = infile.read()
        f.write(content)

    return path

def run_synthesizer(path):
    output = subprocess.check_output([SKETCH_BINARY_PATH, path])

    return output

def write_output(outfile, output):
    outfile.write(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args(sys.argv[1:])
    infile = args.infile
    outfile = args.outfile

    path = write_temp_file(infile, outfile)
    output = run_synthesizer(path)
    write_output(outfile, output)

    infile.close()
    outfile.close()

if __name__=="__main__":
    main()