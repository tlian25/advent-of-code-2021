# Day 10. Syntax Scoring
# https://adventofcode.com/2021/day/10

from collections import deque
from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(10)
    return lines

# Corrupted = closed with wrong character
CLOSE_MATCH = {'(': ')', '{': '}', '[': ']', '<': '>'}
OPENERS = {'(', '{', '[', '<'}
CLOSERS = {')', '}', ']', '>'}

CORRUPT = "corrupt"
INCOMPLETE = "incomplete"
COMPLETE = "complete"


def check_status(line):
    stack = []
    for l in line:
        if l in OPENERS:
            stack.append(l)
        elif l in CLOSERS:
            if not stack:
                return l
            
            if CLOSE_MATCH[stack.pop()] != l:
                return CORRUPT, l
    
    if stack:
        return INCOMPLETE, stack
    return COMPLETE, None


POINT_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}


def solution1():
    lines = parse_lines()
    
    score = 0
    for l in lines:
        status, v = check_status(l)
        
        if status == INCOMPLETE:
            pass
        elif status == COMPLETE:
            pass
        elif status == CORRUPT:
            score += POINT_MAP[v]
        else:
            raise ValueError("Unexpected status")
            
    return score
            


def complete(stack):
    print(stack)
    stack.reverse()
    comp = []
    for s in stack:
        comp.append(CLOSE_MATCH[s])
    print(comp)
    print()
    return comp
        
POINT_MAP2 = {')': 1, ']': 2, '}': 3, '>': 4}


def score(stack):
    ttl = 0
    for s in stack:
        ttl *= 5
        ttl += POINT_MAP2[s]
    return ttl 
    
def solution2():
    lines = parse_lines()
    
    scrs = []
    for l in lines:
        status, v = check_status(l)
        
        if status == CORRUPT:
            pass
        elif status == COMPLETE:
            pass
        elif status == INCOMPLETE:
            comp = complete(v)
            scrs.append(score(comp))
        else:
            raise ValueError("Unexpected status")
            
    # Find median
    scrs.sort()
    return scrs[len(scrs) // 2]
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
