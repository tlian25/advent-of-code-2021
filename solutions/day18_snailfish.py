# Day 18: Snailfish
# https://adventofcode.com/2021/day/18

from collections import deque
from itertools import permutations
from util.input_util import read_input_file


def parse_equation(l):
    s = deque()
    n = ''
    for x in l:
        if x in ('[', ']'):
            if n != '':
                s.append(int(n))
                n = ''
            s.append(x)
        elif x == ',':
            if n != '':
                s.append(int(n))
                n = ''
        else:
            n += x
    return s
            

def parse_lines():
    lines = read_input_file(18)
    eqs = []
    for l in lines:
        #eqs.append(eval(l))
        eqs.append(parse_equation(l))
    return eqs

# Every snailfish is a pair.
# Ordered list of two elements.
# Each element is a regular number or another pair

# If any pair is nested inside four pairs, the leftmost pair explodes
# If any regular number is >= 10, the leftmost number splits

# To explode -> the pair's left value is added to first regular value to the left of pair

def printeq(eq):
    print(' '.join([str(x) for x in eq]))


def explode(eq):

    modified = False
    level = 0
    stack = deque()
    while eq:
        x = eq.popleft()
        if x == '[':
            level += 1
            stack.append(x)
        elif x == ']':
            stack.append(x)
            level -= 1
        # Number
        else:
            # Explode - should be two numbers
            # Pop entire [x, y] off and replace with 0
            if level >= 5:
                modified = True
                left = x
                # Check if there is a deeper nest
                if eq[0] == '[':
                    stack.append(x)
                    continue
                
                # No deeper nest
                right = eq.popleft()
                
                # add left to previous number in stack
                stack.pop()
                i = len(stack)-1
                while i >= 0:
                    if isinstance(stack[i], int):
                        stack[i] += left
                        break
                    i -= 1
                
                close_bracket = eq.popleft()
                stack.append(0)
                # add right to next number in eq
                i = 0
                while i < len(eq):
                    if isinstance(eq[i], int):
                        eq[i] += right
                        break
                    i += 1
                
                return stack + eq, modified
        
            else:
                stack.append(x)
                
    return stack, modified


def split(eq):
    modified = False
    stack = deque()

    while eq:
        x = eq.popleft()
        if isinstance(x, int) and x >= 10:
            modified = True
            stack += deque(['[', x//2, x-x//2, ']']) + eq
            return stack, modified
        else:
            stack.append(x)

    return stack, modified


def magnitude(eq):
    # 3 times left + 2 times right
    stack = deque()
    while eq:
        x = eq.popleft()
        if x != ']':
            stack.append(x)
        # Unwind
        elif x == ']':
            right = stack.pop()
            left = stack.pop()
            open_bracket = stack.pop()
            magn = left * 3 + right * 2
            stack.append(magn)
            
    return stack[0]
            

def add(eq1, eq2):
    eq = eq1 + eq2
    eq.appendleft('[')
    eq.append(']')
    
    # Operate until steady state
    modified = True
    while modified:

        # Explode
        eq, m1 = explode(eq)
        while m1:
            eq, m1 = explode(eq)
        
        # Split
        eq, m2 = split(eq)

        modified = m1 or m2
        
    return eq


def solution1():
    eqs = parse_lines()
    
    eq = eqs[0]
    for i in range(1, len(eqs)):
        eq = add(eq, eqs[i])
    
    return magnitude(eq)


def solution2():
    eqs = parse_lines()
    
    maxmagn = 0
    for eq1, eq2 in permutations(eqs, 2):
        eq = add(eq1, eq2)
        magn = magnitude(eq)
        maxmagn = max(maxmagn, magn)
        
    return maxmagn
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
