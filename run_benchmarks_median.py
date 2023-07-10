import argparse
import sys
import os

from property_synthesizer import PropertySynthesizer

columns = [
    "benchmark_name",
    "num_conjunct", 
    "num_synth_call", 
    "time_synth_call", 
    "num_soundness_call", 
    "time_soundness_call", 
    "num_precision_call",
    "time_precision_call",
    "time_last_call",
    "time_last_iter",
    "time_total"
]

def benchmark_application1():
    #path, num_atom_max, inline_bnd, slv_seed_default, slv_seed_nofreeze
    files = [
        (["application1/sygus/max2.sp"], 3, 5, 128, 64),
        (["application1/sygus/max3.sp"], 3, 5, 128, 64),
        (["application1/sygus/max4.sp"], 4, 5, 32, 32),
        (["application1/sygus/diff.sp"], 3, 5, 128, 128),
        (["application1/sygus/diff2.sp"], 3, 5, 128, 64),
        (["application1/sygus/array_search_2.sp"], 3, 5, 32, 32),
        (["application1/sygus/array_search_3.sp"], 4, 5, 128, 64),
        (["application1/LIA/abs1.sp"], 3, 5, 128, 32),
        (["application1/LIA/abs2.sp"], 3, 5, 64, 64),
        (["application1/list/append.sp"], 3, 10, 32, 128),
        (["application1/list/delete.sp"], 3, 10, 64, 64),
        (["application1/list/deleteFirst.sp"], 3, 10, 64, 64),
        (["application1/list/drop.sp"], 3, 10, 128, 32),
        (["application1/list/elem.sp"], 3, 10, 128, 128),
        (["application1/list/elemIndex.sp"], 3, 10, 128, 128),
        (["application1/list/ith.sp"], 3, 10, 32, 32),
        (["application1/list/min.sp"], 3, 10, 64, 32),
        (["application1/list/replicate.sp"], 3, 10, 64, 64),
        (["application1/list/reverse.sp"], 3, 10, 32, 128),
        (["application1/list/reverse2.sp"], 3, 10, 128, 32),
        (["application1/list/snoc.sp"], 3, 10, 64, 32),
        (["application1/list/stutter.sp"], 3, 10, 32, 32),
        (["application1/list/take.sp"], 3, 10, 32, 128),
        (["application1/tree/empty.sp", "application1/tree/tree.sp"], 3, 5, 128, 128),
        (["application1/tree/branch.sp", "application1/tree/tree.sp"], 3, 5, 128, 64),
        (["application1/tree/elem.sp", "application1/tree/tree.sp"], 3, 5, 32, 128),
        (["application1/tree/branch_left.sp", "application1/tree/tree.sp"], 3, 5, 128, 64),
        (["application1/tree/branch_right.sp", "application1/tree/tree.sp"], 3, 5, 64, 64),
        (["application1/tree/branch_rootval.sp", "application1/tree/tree.sp"], 3, 5, 32, 32),
        (["application1/BST/empty.sp"], 3, 5, 64, 32),
        (["application1/BST/insert.sp"], 3, 5, 128, 32),
        (["application1/BST/delete.sp"], 3, 5, 128, 32),
        (["application1/BST/find.sp"], 3, 5, 64, 32),
        (["application1/stack/empty.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 128, 32),
        (["application1/stack/push.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 128, 128),
        (["application1/stack/pop.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 128, 32),
        (["application1/stack/push_pop.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 64, 32),
        (["application1/queue/empty.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5, 128, 32),
        (["application1/queue/enqueue.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5, 64, 128),
        (["application1/queue/dequeue.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5, 32, 64),
        (["application1/arithmetic/linearSum1.sp"], 3, 5, 64, 64),
        (["application1/arithmetic/linearSum2.sp"], 3, 5, 128, 128),
        (["application1/arithmetic/nonLinearSum1.sp"], 3, 5, 128, 32),
        (["application1/arithmetic/nonLinearSum2.sp"], 3, 5, 64, 64)
    ]

    outfile_default = open("results/application1_default_table.txt", "w")
    outfile_nofreeze = open("results/application1_nofreeze_table.txt", "w")
    statistics_default_list = []
    statistics_nofreeze_list = []

    for (paths, num_atom_max, inline_bnd, default_seed, nofreeze_seed) in files:
        path = paths[0]
        filename = os.path.splitext(path)[0]

        infiles = [open(f"benchmarks/{path}", 'r') for path in paths]

        phi_list, fun_list, statistics = PropertySynthesizer(
            infiles, outfile_default, False, False,
            300, inline_bnd, default_seed,
            num_atom_max, False, False).run()

        with open(f"results/{filename}.txt", "w") as f:
            for n in range(len(phi_list)):
                phi = phi_list[n]
                funs = fun_list[n]

                f.write(f"Property {n}\n\n")
                f.write(str(phi) + "\n")
                for function_name, code in funs:
                    f.write(function_name + "\n")
                    f.write(code + "\n")
                f.write("\n\n")

        statistics_str = [str(x) if isinstance(x, int) else f"{x:.2f}" for x in statistics]
        statistics_default_list.append([filename] + statistics_str)

        for infile in infiles:
            infile.close()

        infiles = [open(f"benchmarks/{path}", 'r') for path in paths]

        phi_list, fun_list, statistics = PropertySynthesizer(
            infiles, outfile_default, False, False,
            300, inline_bnd, nofreeze_seed,
            num_atom_max, False, True).run()

        statistics_str = [str(x) if isinstance(x, int) else f"{x:.2f}" for x in statistics]
        statistics_nofreeze_list.append([filename] + statistics_str)

        for infile in infiles:
            infile.close()

        print(f"{path}: Done")
    
    outfile_default.write(",".join(columns) + "\n")
    for statistics in statistics_default_list:
        outfile_default.write(",".join(statistics) + "\n")

    outfile_nofreeze.write(",".join(columns) + "\n")
    for statistics in statistics_nofreeze_list:
        outfile_nofreeze.write(",".join(statistics) + "\n")

    outfile_default.close()
    outfile_nofreeze.close()

def benchmark_application2():
    pass

def benchmark_application3():
    pass

def benchmark_application4():
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--app1', '-1', dest='app1', action='store_true', default=False)
    parser.add_argument('--app2', '-2', dest='app2', action='store_true', default=False)
    parser.add_argument('--app3', '-3', dest='app3', action='store_true', default=False)
    parser.add_argument('--app4', '-4', dest='app4', action='store_true', default=False)
    parser.add_argument('--all', '-a', dest='all', action='store_true', default=False)

    args = parser.parse_args(sys.argv[1:])

    app1 = args.app1 or args.all
    app2 = args.app2 or args.all
    app3 = args.app3 or args.all
    app4 = args.app4 or args.all
    
    if app1:
        benchmark_application1()

    if app2:
        benchmark_application2()
    
    if app3:
        benchmark_application3()

    if app4:
        benchmark_application4()

if __name__=="__main__":
    main()