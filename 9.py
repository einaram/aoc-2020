import itertools

def parse_input(datatype="input"):
    with open(f"input/9.{datatype}.txt") as infile:
        # return [[x.split()[0], int(x.split()[1])] for x in infile.read().split("\n")]
        return [int(x) for x in infile.read().split("\n")]


def get_preamble(data, idx, length):
    start = idx-length
    return [sum(x) for x in itertools.combinations(data[start:idx], 2) if x[0] != x[1]]


def part1():
    data = parse_input()
    preamble_length = 25
    for r, row in enumerate(data[preamble_length:]):
        if not row in get_preamble(data, r+preamble_length, preamble_length):
            return row
    

assert part1() == 373803594

def part2(infile, requested):
    data = parse_input(infile)
    for i in range(2,500):
        for n, _ in enumerate(data):
            rolling = data[n:n+i]
            if sum(rolling) == requested:
                return min(rolling)+max(rolling)

assert part2('test', 127) == 62
assert part2('input', 373803594)  == 51152360
