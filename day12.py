
from typing import ValuesView
import numpy as np
import math

def read_indata(datatype='test'):
    with open(f"input/12.{datatype}.txt") as infile:
        data = infile.read().split("\n")
        data = [(x[0],int(x[1:])) for x in data]
        return data


def move_in_angle(e, n, d, value):
    if d == 0:
        e += value
    elif d == 90:
        n -=  value
    elif d == 180:
        e -= value
    elif d == 270:
        n += value 
    return e, n, d


def rotate_wp(e, n, instr):
    dir_, d = instr
    if dir_ == 'L':
        d = -d%360

    if d == 90:
        e,n = e,-n 
    elif d == 180:
        e, n = -e, -n
    elif d == 270:
        e, n = -e, n
    return e, n

def part1(data):
    d = 0
    e, n = [0, 0]

    moves = {
        'N': lambda e, n, d, value: (e, n+value, d),
        'S': lambda e, n, d, value: (e,n-value,  d),
        'E': lambda e, n, d, value: (e+value, n, d),
        'W': lambda e, n, d, value: (e-value, n, d),
        'L': lambda e, n, d, value: (e, n, (d-value) % 360),
        'R': lambda e, n, d, value: (e, n, (d+value) % 360),
        'F': move_in_angle 
    }


    instrs= read_indata(data)

    for instr in instrs:
        e, n, d = moves[instr[0]](e, n, d,instr[1] )
    print(e,n,d)
    return abs(e)+abs(n)

def move(e,n, ship, mult):
    ship[0] = ship[0]+e*mult
    ship[1] = ship[1]+n*mult
    return ship

def part2(data):
    e, n = [10, 1]
    ship= [0,0]

    moves = {
        'N': lambda e, n, value: (e, n+value),
        'S': lambda e, n, value: (e,n-value),
        'E': lambda e, n, value: (e+value, n),
        'W': lambda e, n, value: (e-value, n),
    }

    instrs= read_indata(data)

    for instr in instrs:
        if instr[0] in ['N', 'S','E','W']:
            e, n = moves[instr[0]](e, n, instr[1] )
        elif instr[0] in ['L','R']:
            e, n = rotate_wp(e, n, instr)
        elif instr[0] == 'F':
            ship = move(e, n, ship, instr[1])
    print(e,n)
    print(sum((abs(x) for x in ship)))
    return sum((abs(x) for x in ship))

assert part1('test')  == 25
assert part1('input') == 1294

assert part2('test') == 286
part2('input')
