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

def run_benchmark(files, outfile_name, nofreeze = False, write_result_files = False):
    os.makedirs("results", exist_ok=True)
    outfile = open(f"results/{outfile_name}_median.csv", "w")
    statistics_list = []

    for (paths, num_atom_max, inline_bnd, default_seed, nofreeze_seed) in files:
        path = paths[0]
        filename = os.path.splitext(path)[0]
        seed = nofreeze_seed if nofreeze else default_seed

        infiles = [open(f"benchmarks/{path}", 'r') for path in paths]

        phi_list, fun_list, statistics = PropertySynthesizer(
            infiles, outfile, False, False,
            300, inline_bnd, seed,
            num_atom_max, False, nofreeze).run()

        print(f"Done: {filename}, seed = {seed}, nofreeze = {nofreeze}")

        if write_result_files:
            path = f"results/{filename}_median.txt"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
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
        statistics_list.append([filename] + statistics_str)

        for infile in infiles:
            infile.close()

    outfile.write(",".join(columns) + "\n")
    for statistics in statistics_list:
        outfile.write(",".join(statistics) + "\n")

def benchmark_application1():
    #path, num_atom_max, inline_bnd, slv_seed_default, slv_seed_nofreeze
    files = [
        (["application1/sygus/max2.sp"], 3, 5, 32, 64),
        (["application1/sygus/max3.sp"], 3, 5, 128, 64),
        (["application1/sygus/max4.sp"], 4, 5, 128, 128),
        (["application1/sygus/diff.sp"], 3, 5, 128, 64),
        (["application1/sygus/diff2.sp"], 3, 5, 128, 64),
        (["application1/sygus/array_search_2.sp"], 3, 5, 128, 128),
        (["application1/sygus/array_search_3.sp"], 4, 5, 32, 32),
        (["application1/LIA/abs1.sp"], 3, 5, 128, 128),
        (["application1/LIA/abs2.sp"], 3, 5, 128, 64),
        (["application1/list/append.sp"], 3, 10, 64, 64),
        (["application1/list/delete.sp"], 3, 10, 64, 32),
        (["application1/list/deleteFirst.sp"], 3, 10, 128, 64),
        (["application1/list/drop.sp"], 3, 10, 32, 32),
        (["application1/list/elem.sp"], 3, 10, 32, 128),
        (["application1/list/elemIndex.sp"], 3, 10, 128, 32),
        (["application1/list/ith.sp"], 3, 10, 64, 64),
        (["application1/list/min.sp"], 3, 10, 64, 128),
        (["application1/list/replicate.sp"], 3, 10, 64, 128),
        (["application1/list/reverse.sp"], 3, 10, 128, 128),
        (["application1/list/reverse2.sp"], 3, 10, 128, 128),
        (["application1/list/snoc.sp"], 3, 10, 128, 64),
        (["application1/list/stutter.sp"], 3, 10, 128, 128),
        (["application1/list/take.sp"], 3, 10, 128, 128),
        (["application1/tree/empty.sp", "application1/tree/tree.sp"], 3, 5, 64, 128),
        (["application1/tree/branch.sp", "application1/tree/tree.sp"], 3, 5, 128, 128),
        (["application1/tree/elem.sp", "application1/tree/tree.sp"], 3, 5, 128, 128),
        (["application1/tree/branch_left.sp", "application1/tree/tree.sp"], 3, 5, 128, 128),
        (["application1/tree/branch_right.sp", "application1/tree/tree.sp"], 3, 5, 128, 32),
        (["application1/tree/branch_rootval.sp", "application1/tree/tree.sp"], 3, 5, 64, 128),
        (["application1/BST/empty.sp"], 3, 5, 64, 128),
        (["application1/BST/insert.sp"], 3, 5, 128, 128),
        (["application1/BST/delete.sp"], 3, 5, 128, 128),
        (["application1/BST/find.sp"], 3, 5, 32, 32),
        (["application1/stack/empty.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 64, 64),
        (["application1/stack/push.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 64, 64),
        (["application1/stack/pop.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 128, 128),
        (["application1/stack/push_pop.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10, 128, 64),
        (["application1/queue/empty.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5, 32, 32),
        (["application1/queue/enqueue.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5, 32, 128),
        (["application1/queue/dequeue.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5, 32, 32),
        (["application1/arithmetic/linearSum1.sp"], 3, 5, 128, 128),
        (["application1/arithmetic/linearSum2.sp"], 3, 5, 64, 32),
        (["application1/arithmetic/nonLinearSum1.sp"], 3, 5, 32, 128),
        (["application1/arithmetic/nonLinearSum2.sp"], 3, 5, 64, 128)
    ]

    run_benchmark(files, "application1_default", False, True)
    run_benchmark(files, "application1_nofreeze", True, False)

def benchmark_application2():
    files = [
        (["application2/ArrayList/get_add.sp", "application2/ArrayList/list.sp"], 1, 5, 64, 32),
        (["application2/ArrayList/size_new.sp", "application2/ArrayList/list.sp"], 1, 5, 64, 128),
        (["application2/ArrayList/size_add.sp", "application2/ArrayList/list.sp"], 1, 5, 64, 64),
        (["application2/ArraySet/size_new.sp", "application2/ArraySet/set.sp"], 1, 5, 32, 128),
        (["application2/ArraySet/size_add.sp", "application2/ArraySet/set.sp"], 1, 5, 32, 64),
        (["application2/ArraySet/contains_new.sp", "application2/ArraySet/set.sp"], 1, 5, 32, 64),
        (["application2/ArraySet/contains_add.sp", "application2/ArraySet/set.sp"], 1, 5, 32, 128),
        (["application2/ArraySet/remove_new.sp", "application2/ArraySet/set.sp"], 1, 5, 64, 32),
        (["application2/ArraySet/remove_add.sp", "application2/ArraySet/set.sp"], 1, 5, 128, 128),
        (["application2/HashMap/get_new.sp", "application2/HashMap/map.sp"], 1, 5, 32, 128),
        (["application2/HashMap/get_put.sp", "application2/HashMap/map.sp"], 1, 5, 128, 128),
        (["application2/HashMap/put_put.sp", "application2/HashMap/map.sp"], 1, 5, 32, 32),
    ]

    run_benchmark(files, "application2_default", False, True)
    run_benchmark(files, "application2_nofreeze", True, False)

def benchmark_application3():
    files = [
        (["application3/hamming/append.sp", "application3/hamming/list.sp"], 1, 7, 32, 128),
        (["application3/hamming/cons.sp", "application3/hamming/list.sp"], 1, 7, 128, 128),
        (["application3/hamming/cons_delete.sp", "application3/hamming/list.sp"], 1, 7, 64, 64),
        (["application3/hamming/deleteFirst.sp", "application3/hamming/list.sp"], 1, 7, 128, 128),
        (["application3/hamming/delete.sp", "application3/hamming/list.sp"], 1, 7, 32, 32),
        (["application3/hamming/reverse.sp", "application3/hamming/list.sp"], 1, 7, 128, 128),
        (["application3/hamming/snoc.sp", "application3/hamming/list.sp"], 1, 7, 64, 32),
        (["application3/hamming/stutter.sp", "application3/hamming/list.sp"], 1, 7, 128, 128),
        (["application3/hamming/tail.sp", "application3/hamming/list.sp"], 1, 7, 32, 32),
        (["application3/edit/append.sp", "application3/edit/list.sp"], 1, 7, 32, 64),
        (["application3/edit/cons.sp", "application3/edit/list.sp"], 1, 7, 128, 128),
        (["application3/edit/cons_delete.sp", "application3/edit/list.sp"], 1, 7, 32, 64),
        (["application3/edit/deleteFirst.sp", "application3/edit/list.sp"], 1, 7, 32, 32),
        (["application3/edit/delete.sp", "application3/edit/list.sp"], 1, 7, 128, 64),
        (["application3/edit/reverse.sp", "application3/edit/list.sp"], 1, 7, 64, 32),
        (["application3/edit/snoc.sp", "application3/edit/list.sp"], 1, 7, 32, 32),
        (["application3/edit/stutter.sp", "application3/edit/list.sp"], 1, 7, 32, 128),
        (["application3/edit/tail.sp", "application3/edit/list.sp"], 1, 7, 32, 32),
    ]

    run_benchmark(files, "application3_default", False, True)
    run_benchmark(files, "application3_nofreeze", True, False)

def benchmark_application4():
    files = [
        (["application4/conjunction.sp"], 1, 5, 64, 32),
        (["application4/constNeq.sp"], 1, 5, 64, 64),
        (["application4/cube.sp"], 1, 5, 32, 32),
        (["application4/disjunction.sp"], 1, 5, 128, 128),
        (["application4/fourPoints.sp"], 1, 5, 128, 64),
        (["application4/half.sp"], 1, 5, 64, 32),
        (["application4/singlePoint.sp"], 1, 5, 128, 128),
        (["application4/square.sp"], 1, 5, 32, 64),
        (["application4/squareIneq.sp"], 1, 5, 32, 128),
    ]

    run_benchmark(files, "application4_default", False, True)
    run_benchmark(files, "application4_nofreeze", True, False)

def create_log(files):
    for (paths, num_atom_max, inline_bnd, seed) in files:
        path = paths[0]
        filename = os.path.splitext(path)[0]

        infiles = [open(f"benchmarks/{path}", 'r') for path in paths]

        phi_list, fun_list, statistics = PropertySynthesizer(
            infiles, os.devnull, False, True,
            300, inline_bnd, seed,
            num_atom_max, False, False).run()

        print(f"Created detailed log: {filename}, seed = {seed}")

        for infile in infiles:
            infile.close()

def create_logs():
    files = [
        (["application1/tree/branch.sp", "application1/tree/tree.sp"], 3, 5, 128),
        (["application1/arithmetic/nonLinearSum2.sp"], 3, 5, 64)
    ]

    create_log(files)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--app1', '-1', dest='app1', action='store_true', default=False)
    parser.add_argument('--app2', '-2', dest='app2', action='store_true', default=False)
    parser.add_argument('--app3', '-3', dest='app3', action='store_true', default=False)
    parser.add_argument('--app4', '-4', dest='app4', action='store_true', default=False)
    parser.add_argument('--log', '-l', dest='log', action='store_true', default=False)
    parser.add_argument('--all', '-a', dest='all', action='store_true', default=False)

    args = parser.parse_args(sys.argv[1:])

    app1 = args.app1 or args.all
    app2 = args.app2 or args.all
    app3 = args.app3 or args.all
    app4 = args.app4 or args.all
    log = args.log or args.all

    if app1:
        benchmark_application1()

    if app2:
        benchmark_application2()
    
    if app3:
        benchmark_application3()

    if app4:
        benchmark_application4()

    if log:
        create_logs()


if __name__=="__main__":
    main()
