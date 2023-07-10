import argparse
import sys
import os

from spyro_parser import SpyroParser

def compute_expr_size(cxt, memo, expr, bound):
    if bound <= 0:
        return (memo, 0)
    elif expr[0] == 'BINOP':
        memo, size1 = compute_expr_size(cxt, memo, expr[2], bound)
        memo, size2 = compute_expr_size(cxt, memo, expr[3], bound)
        return (memo, size1 * size2)
    elif expr[0] == 'UNARY':
        return compute_expr_size(cxt, memo, expr[2], bound)
    elif expr[0] == 'INT':
        return (memo, 1)
    elif expr[0] == 'VAR':
        symbol = expr[1]
        if symbol in cxt:
            return compute_rule_size(cxt, memo, symbol, bound - 1)
        else:
            return (memo, 1)
    elif expr[0] == 'HOLE':
        size = 2147483648 if expr[1] == 0 else 2 ** int(expr[1])
        return (memo, size)
    elif expr[0] == 'FCALL':
        code = ''
        arg_size = 1
        for e in expr[2]:
            memo, size = compute_expr_size(cxt, memo, e, bound)
            arg_size *= size

        if (expr[1] == 'compare'):
            return (memo, 6 * arg_size)
        else:
            return (memo, arg_size)
    elif expr[0] == 'LAMBDA':
        return compute_expr_size(cxt, memo, expr[2], bound)
    else:
        raise Exception(f'Unhandled case: {expr}')

def compute_rule_size(cxt, memo, symbol, bound):
    if bound <= 0:
        return (memo, 0)

    if symbol in memo.keys():
        return (memo, memo[symbol])

    expr_list = cxt[symbol]
    size_list = []
    for expr in expr_list:
        memo, size = compute_expr_size(cxt, memo, expr, bound)
        size_list.append(size)
    
    size = sum(size_list)
    return (memo, size)

def compute_size(generator, bnd):
    cxt = {symbol:exprlist for (typ, symbol, exprlist) in generator}
    memo = {}

    return compute_rule_size(cxt, memo, generator[0][1], bnd)

def size_application1():
    #path, num_atom_max, inline_bnd
    files = [
        (["application1/sygus/max2.sp"], 3, 5),
        (["application1/sygus/max3.sp"], 3, 5),
        (["application1/sygus/max4.sp"], 4, 5),
        (["application1/sygus/diff.sp"], 3, 5),
        (["application1/sygus/diff2.sp"], 3, 5),
        (["application1/sygus/array_search_2.sp"], 3, 5),
        (["application1/sygus/array_search_3.sp"], 4, 5),
        (["application1/LIA/abs1.sp"], 3, 5),
        (["application1/LIA/abs2.sp"], 3, 5),
        (["application1/list/append.sp"], 3, 10),
        (["application1/list/delete.sp"], 3, 10),
        (["application1/list/deleteFirst.sp"], 3, 10),
        (["application1/list/drop.sp"], 3, 10),
        (["application1/list/elem.sp"], 3, 10),
        (["application1/list/elemIndex.sp"], 3, 10),
        (["application1/list/ith.sp"], 3, 10),
        (["application1/list/min.sp"], 3, 10),
        (["application1/list/replicate.sp"], 3, 10),
        (["application1/list/reverse.sp"], 3, 10),
        (["application1/list/reverse2.sp"], 3, 10),
        (["application1/list/snoc.sp"], 3, 10),
        (["application1/list/stutter.sp"], 3, 10),
        (["application1/list/take.sp"], 3, 10),
        (["application1/tree/empty.sp", "application1/tree/tree.sp"], 3, 5),
        (["application1/tree/branch.sp", "application1/tree/tree.sp"], 3, 5),
        (["application1/tree/elem.sp", "application1/tree/tree.sp"], 3, 5),
        (["application1/tree/branch_left.sp", "application1/tree/tree.sp"], 3, 5),
        (["application1/tree/branch_right.sp", "application1/tree/tree.sp"], 3, 5),
        (["application1/tree/branch_rootval.sp", "application1/tree/tree.sp"], 3, 5),
        (["application1/BST/empty.sp"], 3, 5),
        (["application1/BST/insert.sp"], 3, 5),
        (["application1/BST/delete.sp"], 3, 5),
        (["application1/BST/find.sp"], 3, 5),
        (["application1/stack/empty.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10),
        (["application1/stack/push.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10),
        (["application1/stack/pop.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10),
        (["application1/stack/push_pop.sp", "application1/stack/list.sp", "application1/stack/stack.sp"], 3, 10),
        (["application1/queue/empty.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5),
        (["application1/queue/enqueue.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5),
        (["application1/queue/dequeue.sp", "application1/queue/list.sp", "application1/queue/queue.sp"], 3, 5),
        (["application1/arithmetic/linearSum1.sp"], 3, 5),
        (["application1/arithmetic/linearSum2.sp"], 3, 5),
        (["application1/arithmetic/nonLinearSum1.sp"], 3, 5),
        (["application1/arithmetic/nonLinearSum2.sp"], 3, 5)
    ]

    outfile = open("results/application1_grammar_size.csv", "w")

    for (paths, num_disjunct, inline_bnd) in files:
        path = paths[0]
        with open(f"benchmarks/{path}", 'r') as infile:
            template = infile.read()
            generator = SpyroParser(template).get_generator_rules()
            memo, size = compute_size(generator, inline_bnd)
            filename = os.path.splitext(path)[0]

            outfile.write(f'{filename}, {size ** num_disjunct}\n')

    outfile.close()      

def size_application2():
    files = [
        (["application2/ArrayList/get_add.sp", "application2/ArrayList/list.sp"], 1, 5),
        (["application2/ArrayList/size_new.sp", "application2/ArrayList/list.sp"], 1, 5),
        (["application2/ArrayList/size_add.sp", "application2/ArrayList/list.sp"], 1, 5),
        (["application2/ArraySet/size_new.sp", "application2/ArraySet/set.sp"], 1, 5),
        (["application2/ArraySet/size_add.sp", "application2/ArraySet/set.sp"], 1, 5),
        (["application2/ArraySet/contains_new.sp", "application2/ArraySet/set.sp"], 1, 5),
        (["application2/ArraySet/contains_add.sp", "application2/ArraySet/set.sp"], 1, 5),
        (["application2/ArraySet/remove_new.sp", "application2/ArraySet/set.sp"], 1, 5),
        (["application2/ArraySet/remove_add.sp", "application2/ArraySet/set.sp"], 1, 5),
        (["application2/HashMap/get_new.sp", "application2/HashMap/map.sp"], 1, 5),
        (["application2/HashMap/get_put.sp", "application2/HashMap/map.sp"], 1, 5),
        (["application2/HashMap/put_put.sp", "application2/HashMap/map.sp"], 1, 5),
    ]

    outfile = open("results/application2_grammar_size.csv", "w")

    for (paths, num_disjunct, inline_bnd) in files:
        path = paths[0]
        with open(f"benchmarks/{path}", 'r') as infile:
            template = infile.read()
            generator = SpyroParser(template).get_generator_rules()
            memo, size = compute_size(generator, inline_bnd)
            filename = os.path.splitext(path)[0]

            outfile.write(f'{filename}, {size ** num_disjunct}\n')

    outfile.close() 

def size_application3():
    files = [
        (["application3/hamming/append.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/cons.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/cons_delete.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/deleteFirst.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/delete.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/reverse.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/snoc.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/stutter.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/hamming/tail.sp", "application3/hamming/list.sp"], 1, 7),
        (["application3/edit/append.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/cons.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/cons_delete.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/deleteFirst.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/delete.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/reverse.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/snoc.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/stutter.sp", "application3/edit/list.sp"], 1, 7),
        (["application3/edit/tail.sp", "application3/edit/list.sp"], 1, 7),
    ]

    outfile = open("results/application3_grammar_size.csv", "w")

    for (paths, num_disjunct, inline_bnd) in files:
        path = paths[0]
        with open(f"benchmarks/{path}", 'r') as infile:
            template = infile.read()
            generator = SpyroParser(template).get_generator_rules()
            memo, size = compute_size(generator, inline_bnd)
            filename = os.path.splitext(path)[0]

            outfile.write(f'{filename}, {size ** num_disjunct}\n')

    outfile.close() 

def size_application4():
    files = [
        (["application4/conjunction.sp"], 1, 5),
        (["application4/constNeq.sp"], 1, 5),
        (["application4/cube.sp"], 1, 5),
        (["application4/disjunction.sp"], 1, 5),
        (["application4/fourPoints.sp"], 1, 5),
        (["application4/half.sp"], 1, 5),
        (["application4/singlePoint.sp"], 1, 5),
        (["application4/square.sp"], 1, 5),
        (["application4/squareIneq.sp"], 1, 5),
    ]

    outfile = open("results/application4_grammar_size.csv", "w")

    for (paths, num_disjunct, inline_bnd) in files:
        path = paths[0]
        with open(f"benchmarks/{path}", 'r') as infile:
            template = infile.read()
            generator = SpyroParser(template).get_generator_rules()
            memo, size = compute_size(generator, inline_bnd)
            filename = os.path.splitext(path)[0]

            outfile.write(f'{filename}, {size ** num_disjunct}\n')

    outfile.close() 

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
        size_application1()

    if app2:
        size_application2()
    
    if app3:
        size_application3()

    if app4:
        size_application4()

if __name__ == "__main__":
    main()