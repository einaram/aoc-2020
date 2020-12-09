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
        r = r+preamble_length
        preamble=get_preamble(data,r, preamble_length)
        if not row in preamble:
            break 
    return row

assert part1() == 373803594

def part2(infile, requested):
    data = parse_input(infile)

    for i in range(0,500):
        end= i+2
        for n, _ in enumerate(data):
            rolling = data[n:n+end]
            if sum(rolling) == requested:
                z= min(rolling)+max(rolling)

        # WIP
        # x=[data[n+start:n+stop] for n, _ in enumerate(data) if sum(data[n+start:n+stop]) == requested]
        # if x:
        #     print("x", min(x)+max(x), z)
        #     break
    return z


# part2('test', 127)
assert part2('input', 373803594)  == 51152360
