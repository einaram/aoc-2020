import itertools

def parse_input(datatype="input"):
    with open(f"input/9.{datatype}.txt") as infile:
        return [int(x) for x in infile.read().split("\n")]


def preamble_combos(data, idx, length):
    start = idx-length
    return [sum(x) for x in itertools.combinations(data[start:idx], 2) if x[0] != x[1]]


def part1():
    data = parse_input()
    pream_l = 25
    return next(row for r,row in enumerate(data[pream_l:]) if not row in preamble_combos(data, r+pream_l, pream_l)) # life peak oneliner


assert part1() == 373803594

def part2(infile, requested):
    data = parse_input(infile)
    for i in range(2,500):
        for n in range(len(data)):
            rolling = data[n:n+i]
            if sum(rolling) == requested:
                return min(rolling)+max(rolling)

assert part2('test', 127) == 62
assert part2('input', 373803594)  == 51152360
