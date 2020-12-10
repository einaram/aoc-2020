import numpy as np
def parse_input(datatype="input"):
    with open(f"input/10.{datatype}.txt") as infile:
        return [int(x) for x in infile.read().split("\n")]


def get_adapters(data='input'):
    adapters = np.array(sorted(parse_input(data)))
    adapters = np.append([0], adapters)
    return adapters


jolt=[4]
adpt_max = max([19])

a = get_adapters('input')
def get_next(adapters, in_branch):
    combos = []
    possible = find_possible(adapters, in_branch)
    for pos in possible:
        combos.append(pos)
    if not possible.size == 0:
        return combos
    else:
        return None


def find_possible(adapters, jolt):
    condition = (adapters - jolt >= 1) & (adapters - jolt <= 3)
    possible_adapters = adapters[condition]
    return possible_adapters

combos = [[0]]
iter_count = 0
for jolt in range(100):
    for b,branch in enumerate(combos):
        ret= get_next(a, branch)
        if ret:
            combos.remove(branch)
            combos.extend(ret)
        iter_count +=1
        if iter_count %10000000 == 0:
            print(iter_count)

print(len(combos))
print(len([x for x in combos if x >=max(a)-3]))



    # if max(jolt) >= adpt_max:
    #     break
