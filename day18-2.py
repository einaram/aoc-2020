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
    while inner := re.search(r"\([\d\s\+]+\)", in_str):
        inner_c = inner.group().strip(')').strip('(').strip()
        inner_c = calc_inner_add(inner_c)
        inner_c = calc_inner_par(inner_c)
        in_str = in_str[0:inner.span()[0]] + inner_c + in_str[inner.span()[1]:]
    while inner := re.search(r"\([\d\s\*\+]+\)", in_str):
        inner_c = inner.group().strip(')').strip('(').strip()
        inner_c = calc_inner_add(inner_c)
        inner_c = calc_inner_par(inner_c)
        in_str = in_str[0:inner.span()[0]] + inner_c + in_str[inner.span()[1]:]
    return calc_inner_par(in_str)

def calc_inner_add(inr):
    while part := re.search(r'(\d+) (\+) (\d+)', inr):
        inr = inr[0:part.span()[0]] + do_op(*
                                            part.groups()) + inr[part.span()[1]:]
    return inr

def calc_inner_par(inr):
    while part := re.search(r'(\d+) (\+) (\d+)', inr):
        inr = inr[0:part.span()[0]] + do_op(*
                                            part.groups()) + inr[part.span()[1]:]
    while part := re.search(r'(\d+) ([*+]) (\d+)', inr):
        inr = inr[0:part.span()[0]] + do_op(*
                                            part.groups()) + inr[part.span()[1]:]
    return inr


assert calc_replace("1 + (2 * 3) + (4 * (5 + 6))") == '51'
assert calc_replace("2 * 3 + (4 * 5)") == '46'
assert calc_replace("5 + (8 * 3 + 9 + 3 * 4 * 3)") == '1445'
assert calc_replace("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == '669060'
assert calc_replace(
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == '23340'


s = sum([int(calc_replace(x))  for x in read_indata(datatype='input')]) 

assert s == 93000656194428
print(s)

