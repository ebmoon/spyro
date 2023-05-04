import argparse
import sys
import os

from property_synthesizer import PropertySynthesizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true', default=False)
    parser.add_argument('--disable-min', dest='disable_min', action='store_true', default=False)
    parser.add_argument('--keep-neg-may', dest='keep_neg_may', action='store_true', default=False)
    parser.add_argument('--slv-seed', dest='slv_seed', type=int, nargs='?', default=0)

    args = parser.parse_args(sys.argv[1:])
    outfile = args.outfile
    v = args.verbose
    disable_min = args.disable_min
    keep_neg_may = args.keep_neg_may
    slv_seed = args.slv_seed

    files = [os.path.join(dp, f) for dp, dn, fn in os.walk("./more_examples/bvineq/4bit") for f in fn if ('.sp' in f)]

    seeds = [32, 64, 128]

    for slv_seed in seeds:
        of = open(f"../benchmark_results/bv_{slv_seed}.csv", "w")

        for path in files:
            with open(path, 'r') as infile:
                inline_bnd = 5
                
                # lf = open("./more_examples/jlibsketch/ArraySet/set.sp", "r")

                # num_atom_max = 3
                # num_atom_max = 4 if ("array_search_3" in path) or ("max4" in path) else num_atom_max

                num_atom_max = 1

                # To-Do: Update to include multiple files
                infiles = [infile]

                print(infiles)

                PropertySynthesizer(
                    infiles, of, v, False,
                    300, inline_bnd, slv_seed,
                    num_atom_max, disable_min, keep_neg_may).run()

                # lf.close()
        
        of.close()

    outfile.close()

if __name__=="__main__":
    main()