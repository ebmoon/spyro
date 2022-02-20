import argparse
import sys
import os

from property_synthesizer import PropertySynthesizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args(sys.argv[1:])
    infile = args.infile
    outfile = args.outfile

    PropertySynthesizer(infile, outfile).run()

    infile.close()
    outfile.close()

if __name__=="__main__":
    main()