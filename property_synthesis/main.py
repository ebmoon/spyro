import argparse
import subprocess
import sys

SKETCH_BINARY_PATH = "./sketch-frontend/sketch"

def run_synthesizer(filename):
    output = subprocess.check_output([SKETCH_BINARY_PATH, filename])

    return output

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', type=str)

    args = parser.parse_args(sys.argv[1:])
    filename = args.file

    print(run_synthesizer(filename))

if __name__=="__main__":
    main()