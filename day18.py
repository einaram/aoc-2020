import re
import math


def read_indata(datatype='test'):
    with open(f"input/18.{datatype}.txt") as infile:
        data = infile.read().split("\n")
        return data

def do_operation(p1, op, p2):
    ops = {'+': sum,
           '*': math.prod}
    return str(ops[op]([int(p1), int(p2)]))


def calc_replace(in_str):
    while inner := re.search(r"\([\d\s\*\+]+\)", in_str):
        inner_c = inner.group().strip(')').strip('(').strip()
        inner_c = calculate_inner(inner_c)
        in_str = in_str[0:inner.span()[0]] + inner_c + in_str[inner.span()[1]:]
    return calculate_inner(in_str)


def calculate_inner(inner_c):
    while part := re.search(r'(\d+) ([*+]) (\d+)', inner_c):
        inner_c = inner_c[0:part.span()[0]] + do_operation(*
                                                           part.groups()) + inner_c[part.span()[1]:]
    return inner_c


assert calc_replace("2 * 3 + (4 * 5)") == '26'
assert calc_replace("5 + (8 * 3 + 9 + 3 * 4 * 3)") == '437'
assert calc_replace("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == '12240'


s = sum([int(calc_replace(x)) for x in read_indata(datatype='input')])
print(s)