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
    parser.add_argument('--inline-bnd', dest='inline_bnd', type=int, nargs='?', default=5)
    parser.add_argument('--inline-bnd-sound', dest='inline_bnd_sound', type=int, nargs='?', default=10)
    parser.add_argument('--num-atom-max', dest='num_atom_max', type=int, nargs='?', default=3)
    parser.add_argument('--minimize-terms', dest='minimize_terms', action='store_true', default=False)
    parser.add_argument('--keep-neg-may', dest='keep_neg_may', action='store_true', default=False)

    args = parser.parse_args(sys.argv[1:])
    infile = args.infile
    outfile = args.outfile
    v = args.verbose
    write_log = args.write_log
    inline_bnd = args.inline_bnd
    inline_bnd_sound = args.inline_bnd_sound
    num_atom_max = args.num_atom_max
    minimize_terms = args.minimize_terms
    keep_neg_may = args.keep_neg_may

    PropertySynthesizer(
        infile, outfile, v, write_log,
        inline_bnd, inline_bnd_sound, 
        num_atom_max, minimize_terms, keep_neg_may).run()

    infile.close()
    outfile.close()

if __name__=="__main__":
    main()