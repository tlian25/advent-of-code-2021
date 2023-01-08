# Day 5. Hydrothermal Venture 
# https://adventofcode.com/2021/day/5

from collections import defaultdict
from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(5)

    arr = []
    for l in lines:
        p1, p2 = l.split(' -> ')

        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        
        arr.append((int(x1), int(y1), int(x2), int(y2)))
        
    return arr


def count_points(points:dict):
    count = 0
    for p, v in points.items():
        if v > 1:
            count += 1
    
    return count



def solution1():
    lines = parse_lines()
    
    points = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        
        # vertical
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            
            for y in range(y1, y2+1):
                points[(x1, y)] += 1
            
        # horizontal
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            
            for x in range(x1, x2+1):
                points[(x, y1)] += 1
    
    # Count points that have more than 1 line going across
    return count_points(points)
    
    

    
def solution2():
    lines = parse_lines()
    
    points = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        
        # vertical
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            
            for y in range(y1, y2+1):
                points[(x1, y)] += 1
            
        # horizontal
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            
            for x in range(x1, x2+1):
                points[(x, y1)] += 1
                
        # Diagonal
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            
            if y1 < y2:
                diff = 1
            else:
                diff = -1
                
            while x1 <= x2:
                points[(x1, y1)] += 1
                x1 += 1
                y1 += diff
    
    # Count points that have more than 1 line going across
    return count_points(points)
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
