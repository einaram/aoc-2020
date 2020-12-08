def parse_input(datatype="input"):
    with open(f"input/8.{datatype}.txt") as infile:
        return [[x.split()[0], int(x.split()[1])] for x in infile.read().split("\n")]


class EndOfInstruction(Exception):
    pass

class InstructionsFinnished(Exception):
    pass

class GameConsole():
    def __init__(self, instr) -> None:
        self.accumulator = 0
        self.idx = 0
        self.last_acc = 0
        self.instr = instr
        self.used_calls = [False]*len(instr)

    def acc(self, arg):
        self.accumulator += int(arg)
        self.idx +=1

    def jmp(self, arg):
        self.idx += arg

    def nop(self,arg):
        self.idx +=1

    def call_instr(self):
        self.last_acc = self.accumulator
        getattr(self, self.instr[self.idx][0])(
            self.instr[self.idx][1])

        
    def next(self):
        curr_idx = self.idx
        if self.used_calls[curr_idx]:
            raise EndOfInstruction
          
        self.call_instr()
        self.used_calls[curr_idx] = True

        try:
            self.instr[self.idx] #raises at end of list
        except Exception as E:
            print("End of list. Acc:", self.accumulator)
            raise InstructionsFinnished

# TODO rewrite with __next__()


def part1():
    gameconsole = GameConsole(parse_input())
    while True:
        try:
            gameconsole.next()
        except Exception as e:
            print(e)
            print("Done", gameconsole.last_acc, gameconsole.accumulator)
            break
    return gameconsole.accumulator
assert part1() == 1331
# Part 2

def part2_runner(input_):
    gameconsole = GameConsole(input_)
    i = 0
    while True:
        try:
            gameconsole.next()
        except EndOfInstruction:
            break
        except InstructionsFinnished as E:
            return gameconsole.accumulator

def part2():
    instr = parse_input()
    for change_idx in [i for i, item in enumerate(instr) if item[0] in ['jmp', 'nop']]:
        instr_tmp = [x.copy() for x in instr]
        instr_tmp[change_idx][0] = 'jmp' if instr_tmp[change_idx][0] == 'nop' else 'nop'
        gamecon_exitcode = part2_runner(instr_tmp)
        if gamecon_exitcode:
            return gamecon_exitcode
assert part2() == 1121 
# 1121
