# Day 24. Arithmetic Logic Unit
# https://adventofcode.com/2021/day/24

import json
import sys
from copy import deepcopy
from collections import deque
from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(24)
    operations = []
    for i, l in enumerate(lines):
        operations.append(l.split(' '))
    return operations

W, X, Y, Z = 'w', 'x', 'y', 'z'
INP, ADD, MUL, DIV, MOD, EQL = 'inp', 'add', 'mul', 'div', 'mod', 'eql'

def inp(vals, a, v) -> None:
    vals[a] = v

def add(vals, a, b) -> None:
    vals[a] += bvalue(vals, b)

def mul(vals, a, b) -> None:
    vals[a] *= bvalue(vals, b)

def div(vals, a, b) -> None:
    vals[a] //= bvalue(vals, b)

def mod(vals, a, b):
    vals[a] %= bvalue(vals, b)
    
def eql(vals, a, b):
    vals[a] = 1 if vals[a] == bvalue(vals, b) else 0
    
def bvalue(vals, b) -> int:
    return vals[b] if b in vals else int(b)


OPMAP = {INP: inp, ADD: add, MUL: mul, DIV: div, MOD: mod, EQL: eql}
def operate(vals, *args) -> None:
    OPMAP[args[0]](vals, *args[1:])
    


OPERATIONS = parse_lines()
CACHE = [{} for _ in range(14)] # Cache each digit place
INP_INDEX = []

def populate_cache():
    nums = [9 for _ in range(14)]
    cache_idx = 0
    vals = {W:0, X:0, Y:0, Z:0}
    for i, op in enumerate(OPERATIONS):
        if op[0] == INP:
            n = nums[cache_idx]
            operate(vals, *op, n)
            CACHE[cache_idx][n] = deepcopy(vals)
            cache_idx += 1
            INP_INDEX.append(i)
        else:
            operate(vals, *op)
    
populate_cache()
print(INP_INDEX)


def num_to_inputs(numstr) -> list:
    l = [int(s) for s in str(numstr)]
    return l if 0 not in l else []


# Clear all caches to the right of i
def clear_caches(start):
    for i in range(start, 14):
        CACHE[i].clear()


NUM = [0 for _ in range(14)]

L = len(OPERATIONS)
def dfs(vals, n, i):
    inp_index = INP_INDEX[i]
    NUM[i] = n
    print(f"\rDFS: {NUM} - {n} - {i} - {inp_index} - {vals}", end="")
    inp_op = OPERATIONS[inp_index]
    operate(vals, *inp_op, n)
    
    for j in range(inp_index+1, L):
        op = OPERATIONS[j]
        if op[0] == INP:
            for n in range(9, 0, -1):
                dfs(deepcopy(vals), n, i+1)
        else:
            operate(vals, *op)
    
    if vals[Z] == 0:
        print()
        print(NUM)
        sys.exit()
        
        
    
    
        
vals = {W:0, X:0, Y:0, Z:0}

dfs(vals, 9, 0)
    
    


def solution1():
    pass
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
