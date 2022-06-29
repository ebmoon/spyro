import argparse
import sys
import os

from template_parser import TemplateParser

def compute_expr_size(cxt, memo, expr):
    if expr[0] == 'BINOP':
        memo, size1 = compute_expr_size(cxt, memo, expr[2])
        memo, size2 = compute_expr_size(cxt, memo, expr[3])
        return (memo, size1 * size2)
    elif expr[0] == 'UNARY':
        return compute_expr_size(cxt, memo, expr[2])
    elif expr[0] == 'INT':
        return (memo, 1)
    elif expr[0] == 'VAR':
        symbol = expr[1]
        if symbol in cxt:
            return compute_rule_size(cxt, memo, symbol)
        else:
            return (memo, 1)
    elif expr[0] == 'HOLE':
        size = 2147483648 if expr[1] == 0 else 2 ** int(expr[1])
        return (memo, size)
    elif expr[0] == 'FCALL':
        code = ''
        arg_size = 1
        for e in expr[2]:
            memo, size = compute_expr_size(cxt, memo, e)
            arg_size *= size

        if (expr[1] == 'compare'):
            return (memo, 6 * arg_size)
        else:
            return (memo, arg_size)
    elif expr[0] == 'LAMBDA':
        return compute_expr_size(cxt, memo, expr[2])
    else:
        raise Exception(f'Unhandled case: {expr}')

def compute_rule_size(cxt, memo, symbol):
    if symbol in memo.keys():
        return (memo, memo[symbol])

    expr_list = cxt[symbol]
    size_list = []
    for expr in expr_list:
        memo, size = compute_expr_size(cxt, memo, expr)
        size_list.append(size)
    
    size = sum(size_list)
    if symbol not in memo.keys():
        memo[symbol] = size
    
    return (memo, size)

def compute_size(generator):
    cxt = {symbol:exprlist for (typ, symbol, exprlist) in generator}
    memo = {}

    return compute_rule_size(cxt, memo, generator[0][1])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args(sys.argv[1:])
    outfile = args.outfile

    files = [os.path.join(dp, f) for dp, dn, fn in os.walk("./examples") for f in fn if ('.prop' in f)]
    # files = [os.path.join(dp, f) for dp, dn, fn in os.walk("./difficult_examples") for f in fn if ('.prop' in f)]

    for path in files:
        with open(path, 'r') as infile:
            template = infile.read()
            generator = TemplateParser(template).get_generator_rules()
            memo, size = compute_size(generator)
            basename = os.path.basename(path)
            outfile.write(f'{basename}: {memo} -> {size ** 3} for each clause\n')

    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()