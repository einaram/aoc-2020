import re
import math

def read_indata(datatype='test'):
    with open(f"input/14.{datatype}.txt") as infile:
        data = infile.read().split("\n")
        data = [x.split(" = ") for x in data]
        data = [(k.strip('mem[]'), v) for k, v in data]
        return data


def do_operation(p1, p2, op):
    ops = {'+': sum,
           '*': math.prod}
    p1 = int(p1)
    p2 = int(p2)

    return str(ops[op]([p1, p2]))


def calc(input_):

    # ^ will must be used with [i:]
    match = re.compile(r"(\({1,4}.+\){1,4}|\d+|\*|\+)")

    # does not match second ():
    # match = re.compile(r"(\(.+\)|\d+) (\*|\+) (\(.+\)|\d+)")

    # for m in match.finditer(a):
    # print(m.group(),"end")
    if len(input_) < 3:
        return input_
    if type(input_) == str:
        p1, op, p2, *rest = match.findall(input_)
    else:
        p1, op, p2, *rest = input_
    print(p1,op, p2 )
    if p1.startswith('('):
        p1 = calc(p1[1:-1])[0]
    elif p2.startswith('('):
        p2 = calc(p2[1:-1])[0]

    return calc([do_operation(p1, p2, op)] + rest)


def clean(result):
    return int(result[0])


assert clean(calc("2 * 3 + (4 * 5)")) == 26
assert clean(calc("5 + (8 * 3 + 9 + 3 * 4 * 3)")) == 437
assert clean(calc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")) == 12240

# fails:
assert clean(calc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")) == 13632
# . regex  finds ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2
