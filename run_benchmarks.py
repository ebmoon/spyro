import argparse
import sys
import os

from property_synthesizer import PropertySynthesizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true', default=False)
    parser.add_argument('--num-atom-max', dest='num_atom_max', type=int, nargs='?', default=3)
    parser.add_argument('--minimize-terms', dest='minimize_terms', action='store_true', default=False)
    
    args = parser.parse_args(sys.argv[1:])
    outfile = args.outfile
    v = args.verbose
    inline_bnd_sound = 10
    num_atom_max = args.num_atom_max
    minimize_terms = args.minimize_terms

    files = [os.path.join(dp, f) for dp, dn, fn in os.walk("./examples") for f in fn if ('.prop' in f)]

    for path in files:
        with open(path, 'r') as infile:
            inline_bnd = 10 if "list" in path else 5
            PropertySynthesizer(infile, outfile, v, inline_bnd, inline_bnd_sound, num_atom_max, minimize_terms).run_benchmark()

    outfile.close()

if __name__=="__main__":
    main()