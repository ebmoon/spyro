import argparse
import sys
import os

from property_synthesizer import PropertySynthesizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('--write-log', dest='write_log', action='store_true', default=False)
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true', default=False)
    parser.add_argument('--timeout', dest='timeout', type=int, nargs='?', default=300)
    parser.add_argument('--inline-bnd', dest='inline_bnd', type=int, nargs='?', default=5)
    parser.add_argument('--num-atom-max', dest='num_atom_max', type=int, nargs='?', default=3)
    parser.add_argument('--disable-min', dest='disable_min', action='store_true', default=False)
    parser.add_argument('--keep-neg-may', dest='keep_neg_may', action='store_true', default=False)

    args = parser.parse_args(sys.argv[1:])
    infile = args.infile
    outfile = args.outfile
    v = args.verbose
    write_log = args.write_log
    timeout = args.timeout
    inline_bnd = args.inline_bnd
    num_atom_max = args.num_atom_max
    disable_min = args.disable_min
    keep_neg_may = args.keep_neg_may

    PropertySynthesizer(
        infile, outfile, v, write_log,
        timeout, inline_bnd,
        num_atom_max, disable_min, keep_neg_may).run()

    infile.close()
    outfile.close()

if __name__=="__main__":
    main()