import argparse
import sys
import os

from property_synthesizer import PropertySynthesizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true', default=False)
    parser.add_argument('--disable-min', dest='disable-min', action='store_true', default=False)
    parser.add_argument('--keep-neg-may', dest='keep_neg_may', action='store_true', default=False)

    args = parser.parse_args(sys.argv[1:])
    outfile = args.outfile
    v = args.verbose
    disable_min = args.disable_min
    keep_neg_may = args.keep_neg_may

    files = [os.path.join(dp, f) for dp, dn, fn in os.walk("./examples") for f in fn if ('.prop' in f)]

    for path in files:
        with open(path, 'r') as infile:
            #if not (('max4' in path) or ('max5' in path) or ('branch.prop' in path)):
            #   continue

            if not ('others' in path):
                continue

            inline_bnd = 10 if ("list" in path) or ("stack" in path) or ("normal" in path) else 5
            
            num_atom_max = 3
            num_atom_max = 4 if ("array_search_3" in path) or ("max4" in path) else num_atom_max
            num_atom_max = 5 if ("max5" in path) else num_atom_max

            PropertySynthesizer(
                infile, outfile, v, False,
                300, inline_bnd,
                num_atom_max, disable_min, keep_neg_may).run()

    outfile.close()

if __name__=="__main__":
    main()