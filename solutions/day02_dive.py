# Day 
# https://adventofcode.com/2021/day/

from util.input_util import read_input_file

DIRECTIONS = {'forward': (1, 0),
              'up': (0, -1),
              'down': (0, 1)}



def parse_lines():
    lines = read_input_file(2)
    moves = []
    for l in lines:
        dir, val = l.split(' ')
        dir = DIRECTIONS[dir]
        val = int(val)
        moves.append( (dir[0] * val, dir[1] * val))
        
    return moves
        

def solution1():
    moves = parse_lines()
    x = 0
    y = 0
    
    for m in moves:
        x += m[0]
        y += m[1]
        
    return x * y
    
    
def solution2():
    moves = parse_lines()
    x = 0
    y = 0
    aim = 0
    
    for m in moves:
        x += m[0]
        y += m[0] * aim
        aim += m[1]
        
    return x * y
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
