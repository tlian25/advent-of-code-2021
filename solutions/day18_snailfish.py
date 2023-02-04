# Day 18: Snailfish
# https://adventofcode.com/2021/day/18

from collections import deque
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
    right = 0
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
            if level >= 5 and not modified:
                modified = True
                left = x
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
                level -= 1
                stack.append(0)
                
            else:
                print(x, right)
                printeq(stack)
                stack.append(x+right)
                right = 0
                

        
    return stack, modified


def split(eq):
    modified = False
    stack = deque()
    while eq:
        x = eq.popleft()
        if isinstance(x, int) and x >= 10:
            modified = True
            stack += ['[', x // 2, x - x // 2, ']']
        else:
            stack.append(x)
            
    return stack, modified
                
                    
def process(l):
    pass


def solution1():
    eqs = parse_lines()
    
    eq = eqs[0]
    for i in range(1, 2):
        
        eq += eqs[i]
        eq.appendleft('[')
        eq.append(']')
        
        printeq(eq)
        
        # Operate until steady state
        modified = True
        while modified:
            eq, m1 = explode(eq)
            printeq(eq)

            eq, m2 = split(eq)
            modified = m1 or m2
    
            printeq(eq)
        
    
            
        
    
    
    
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
