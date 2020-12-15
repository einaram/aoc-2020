
from os import read


def read_indata(datatype='test'):
    with open(f"input/14.{datatype}.txt") as infile:
        data = infile.read().split("\n")
        data = [x.split(" = ") for x in data]
        data = [(x[0].strip('mem[]'), x[1]) for x in data]
        return data


def create_mask(mask_str):
    return [(idx, int(val)) for idx, val in enumerate(mask_str) if val !='X']

def apply_mask(mask, bin_val):
    for m in mask:
        bin_val[m[0]] = str(m[1])
    return bin_val
    
mask = []
def part1(datatype):
    data = read_indata(datatype)

    mem = {}
    for row in data:
        if "ask" in row[0]:
            # mask = row[1]
            mask = create_mask(row[1])

        else:
            bin_val = list('{:036b}'.format(int(row[1])))
            mem[row[0]] = int("".join(apply_mask(mask, bin_val)),2)

    mem

    print(sum([int(x) for x in mem.values()]))
    return mem

part1('input')
