# %%
import itertools

with open("1.input.txt") as infile:
    data =infile.readlines()
testdata = """1721
979
366
299
675
1456""".split("\n")

def runnerA(data):
    data = [int(x.strip()) for x in data]

    return [x[0]*x[1] for x in itertools.combinations(data,2) if x[0]+x[1]==2020][0]

assert runnerA(testdata)== 514579
print(runnerA(data))

def runnerB(data):
    data = [int(x.strip()) for x in data]

    return [x[0]*x[1]*x[2] for x in itertools.combinations(data, 3) if x[0]+x[1]+x[2] == 2020][0]


assert runnerB(testdata) == 241861950

print(runnerB(data))
# %%
