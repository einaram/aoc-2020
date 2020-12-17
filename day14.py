
def read_indata(datatype='test'):
    with open(f"input/14.{datatype}.txt") as infile:
        data = infile.read().split("\n")
        data = [x.split(" = ") for x in data]
        data = [(k.strip('mem[]'), v) for k, v in data]
        return data


def create_mask(mask_str):
    return {idx: int(val) for idx, val in enumerate(mask_str) if val != 'X'}


def create_mask2(mask_str):
    return {idx: val for idx, val in enumerate(mask_str)}


def apply_mask1(mask, bin_val):
    for k, v in mask.items():
        bin_val[k] = str(v)
    return bin_val


def to_36bin(value):
    return list('{:036b}'.format(int(value)))


def apply_adr_mask(addr, mask):
    addr = to_36bin(addr)
    new_adrs = [addr]
    ad1 = []
    for i, idx in enumerate(addr):
        m = mask.get(i)
        inner_new_adr = []
        for new_adr in new_adrs:
            if m == '0':
                pass
            elif m == '1':
                new_adr[i] = '1'
            else:  # x
                # 0:
                new_adr[i] = '0'
                # 1
                ad1 = new_adr.copy()
                ad1[i] = '1'

                inner_new_adr.append(ad1)
        new_adrs.extend(inner_new_adr)
    return [int(''.join(x), 2) for x in new_adrs]


def runner(datatype, part=1):
    mask = []
    data = read_indata(datatype)

    mem = {}
    for row in data:
        if "ask" in row[0]:
            mask = create_mask(row[1]) if part == 1 else create_mask2(row[1])
        else:
            bin_val = to_36bin(row[1])
            if part == 1:
                mem[row[0]] = int("".join(apply_mask1(mask, bin_val)), 2)
            elif part == 2:
                for addr in apply_adr_mask(row[0], mask):
                    mem[addr] = row[1]

    mem

    print(sum([int(x) for x in mem.values()]))
    return mem, sum([int(x) for x in mem.values()])


assert runner('input', 1)[1] == 12408060320841

assert runner('test2', 2)[1] == 208
assert runner('input', 2)[1] == 4466434626828
