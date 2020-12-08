def parse_input(datatype="input"):
    with open(f"input/8.{datatype}.txt") as infile:
        return [[x.split()[0], int(x.split()[1])] for x in infile.read().split("\n")]


class GameConsole():
    def __init__(self, instr) -> None:
        self.accumulator = 0
        self.idx = 0
        self.last_acc = 0
        self.instr = instr
        self.instr_len = len(self.instr)
        self.total_calls = 0

    def acc(self, arg):
        self.accumulator += int(arg)
        self.idx +=1

    def jmp(self, arg):
        self.idx += arg

    def nop(self,arg):
        self.idx +=1

    def next1(self):
        curr_idx = self.idx
        getattr(self, self.instr[self.idx][0])(
            self.instr[self.idx][1])
        print(self.last_acc, self.accumulator)

        if self.instr[self.idx] == None:
            print("ACC5")
            exit()

        self.last_acc = self.accumulator
        self.instr[curr_idx] = None

    def next2(self):
        if self.total_calls == self.instr_len:
            raise Exception("end of instructions")
        self.total_calls += 1
        
        getattr(self, self.instr[self.idx][0])(
            self.instr[self.idx][1])
        try:
            self.instr[self.idx] #raises at en of list
        except Exception as E:
            print("end of list. Acc:", self.accumulator)
            raise E

# TODO rewrite with __next__()


def part1():
    gameconsole = GameConsole(parse_input())
    while True:
        try:
            gameconsole.next1()
        except:
            break
# part1()
# Part 2


def part2_runner(input_):
    gameconsole = GameConsole(input_)
    i = 0
    while True:
        try:
            gameconsole.next2()
        except:
            break

def part2():
    instr = parse_input()
    for change_idx in [i for i, item in enumerate(instr) if item[0] in ['jmp', 'nop']]:
        instr_tmp = [x.copy() for x in instr]
        instr_tmp[change_idx][0] = 'jmp' if instr_tmp[change_idx][0] == 'nop' else 'nop'
        part2_runner(instr_tmp)
part2()
# 1121
