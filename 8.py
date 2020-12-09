import copy

def parse_input(datatype="input"):
    with open(f"input/8.{datatype}.txt") as infile:
        return [[x.split()[0], int(x.split()[1])] for x in infile.read().split("\n")]


INSTRUCTION_FINNISHED = 1
END_OF_INSTRUCTION_ERR = 2

def acc(arg, acc, idx):
    acc += arg
    idx += 1
    return acc, idx

def jmp(arg, acc, idx):
    idx += arg
    return acc, idx

def nop(arg, acc, idx):
    idx += 1
    return acc, idx

operations = {
    'acc':acc,
    'jmp': jmp,
    'nop':nop}

def run_console(instrs):
    accum = 0
    idx = 0
    used_calls = [False]*len(instrs)
    err = None

    while True:
        curr_idx = idx
        if used_calls[idx]:
            err = END_OF_INSTRUCTION_ERR
            break  

        accum, idx = operations.get(instrs[idx][0])(
            instrs[idx][1], accum, idx)
        used_calls[curr_idx] = True
        try: #When try is faster then len()..
            instrs[idx]
        except:
            err = INSTRUCTION_FINNISHED
            break
    return err, accum

assert run_console(parse_input())[1] == 1331

# Part 2
def part2():
    instr = parse_input()
    changes = {'nop': 'jmp',
               'jmp': 'nop'}
    for change_idx, new_op in [(i, changes[item[0]]) for i, item in enumerate(instr) if item[0] in changes]:
        instr_tmp = copy.deepcopy(instr)
        instr_tmp[change_idx][0] = new_op

        err, accum = run_console(instr_tmp)
        if err == INSTRUCTION_FINNISHED:
            return accum

assert part2() == 1121 
