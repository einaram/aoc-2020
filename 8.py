import copy

def parse_input(datatype="input"):
    with open(f"input/8.{datatype}.txt") as infile:
        return [[x.split()[0], int(x.split()[1])] for x in infile.read().split("\n")]


INSTRUCTION_FINNISHED = 1
END_OF_INSTRUCTION = 2

class GameConsole():
    def __init__(self, instr) -> None:
        self.accumulator = 0
        self.idx = 0
        self.exit_code = None
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
        getattr(self, self.instr[self.idx][0])(
            self.instr[self.idx][1])

    def __iter__(self):
        return self
        
    def __next__(self):
        curr_idx = self.idx
        if self.used_calls[curr_idx]:
            self.exit_code = END_OF_INSTRUCTION
            raise StopIteration
          
        self.call_instr()
        self.used_calls[curr_idx] = True

        try:
            self.instr[self.idx] #raises at end of list
        except Exception as E:
            self.exit_code = INSTRUCTION_FINNISHED
            raise StopIteration
        return self.accumulator
    def run(self):
        """When to not use an iterator :)"""
        for innstruction in self:
            pass
        return self.accumulator, self.exit_code

def part1():
    gameconsole = GameConsole(parse_input())
    accum, err = gameconsole.run()
    return accum
assert part1() == 1331


# Part 2
def part2():
    instr = parse_input()
    changes = {'nop': 'jmp',
               'jmp': 'nop'}
    for change_idx, new_op in [(i, changes[item[0]]) for i, item in enumerate(instr) if item[0] in changes]:
        instr_tmp = copy.deepcopy(instr)
        instr_tmp[change_idx][0] = new_op

        gameconsole = GameConsole(instr_tmp)
        accum, err = gameconsole.run()
        if err == INSTRUCTION_FINNISHED:
            return accum
    else:
        return None

assert part2() == 1121 
