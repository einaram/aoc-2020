from collections import defaultdict

puzzle = [0,1,4,13,15,12,16]
puzzle_test = [0, 3, 6]

def play(puzzle, end = 2020):
    turn = 1
    puzzle_l = len(puzzle)
    last = defaultdict(lambda: [0, 0])
    while turn <= end:
        if turn <= puzzle_l:
            spoken = puzzle[turn-1]
            last[spoken] = [turn]+[last[spoken][0]]
        elif last[spoken][-1] == 0:
            spoken = 0
            last[spoken] = [turn]+[last[spoken][0]]
        else:
            spoken = last[spoken][0]-last[spoken][1]
            last[spoken] = [turn]+[last[spoken][0]]
        turn +=1 
    print(spoken)
    return spoken


# assert play(puzzle_test) == 436

# assert play(puzzle, 2020) == 1665

play(puzzle, 30000000)
# assert play( [0, 3, 6], 30000000)== 175594
# assert play( [1, 3, 2], 30000000)== 2578
# assert play([2, 1, 3], 30000000) == 3544142
# assert play([1, 2, 3], 30000000) == 261214
# assert play( [2, 3, 1], 30000000)== 6895259
# assert play([3, 2, 1], 30000000) == 18
# assert play([3, 1, 2], 30000000) == 362
