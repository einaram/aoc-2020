import re
import math


def read_indata(datatype='test'):
    with open(f"input/18.{datatype}.txt") as infile:
        data = infile.read().split("\n")
        return data


def do_op(p1, op, p2):
    ops = {'+': sum,
           '*': math.prod}
    return str(ops[op]([int(p1), int(p2)]))


def calc_replace(in_str):
    in_str = calc_parentheses(in_str, op=r'\+')
    in_str = calc_parentheses(in_str, op=r'\*\+')
    return calc_inner_par(in_str)


def calc_parentheses(in_str, op):
    while inner := re.search(rf"\([\d\s{op}]+\)", in_str):
        inner_c = inner.group().strip(')').strip('(').strip()
        inner_c = calc_inner_par(inner_c, )
        in_str = in_str[0:inner.span()[0]] + inner_c + in_str[inner.span()[1]:]
    return in_str


def calc_inner_par(inr):
    inr = calc_inner_par_op(inr, '\+')
    inr = calc_inner_par_op(inr, '[*+]')
    return inr


def calc_inner_par_op(inr, op):
    while part := re.search(fr'(\d+) ({op}) (\d+)', inr):
        inr = inr[0:part.span()[0]] + do_op(*
                                            part.groups()) + inr[part.span()[1]:]
    return inr


assert calc_replace("1 + (2 * 3) + (4 * (5 + 6))") == '51'
assert calc_replace("2 * 3 + (4 * 5)") == '46'
assert calc_replace("5 + (8 * 3 + 9 + 3 * 4 * 3)") == '1445'
assert calc_replace("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == '669060'
assert calc_replace(
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == '23340'


s = sum([int(calc_replace(x)) for x in read_indata(datatype='input')])

assert s == 93000656194428
print(s)
