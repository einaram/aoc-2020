# %%
import itertools
import numpy

with open("1.input.txt") as infile:
    data =infile.readlines()

testdata = """1721
979
366
299
675
1456""".split("\n")

def runner(data,count=2):
    data = [int(x.strip()) for x in data]
    return [numpy.prod(x) for x in itertools.combinations(data, count) if sum(x) == 2020][0]

# A
assert runner(testdata)== 514579
print(runner(data))

# B
assert runner(testdata,3) == 241861950
print(runner(data,3))
# %%


