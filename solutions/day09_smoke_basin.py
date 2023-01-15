# Day 9. Smoke Basin
# https://adventofcode.com/2021/day/9

from util.input_util import read_input_file
from collections import deque

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse_lines():
    lines = read_input_file(9)

    grid = []
    for l in lines:
        grid.append([int(x) for x in l])

    return grid


# Risk level of low point = 1 + height

def check_low_point(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    for dr, dc in DIRS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if grid[nr][nc] <= grid[r][c]:
                return False
    return True
    


def solution1():
    grid = parse_lines()

    R = len(grid)
    C = len(grid[0])
    
    total = 0
    for r in range(R):
        for c in range(C):
            if check_low_point(grid, r, c):
                total += grid[r][c] + 1
    
    return total
    
    

def flood_fill(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    
    # From low point
    q = deque([(r, c)])
    grid[r][c] = '#'

    count = 0
    while q:
        r, c = q.popleft()
        count += 1
        
        for dr, dc in DIRS:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] not in (9, '#'):
                    # mark as seen and add to queue
                    grid[nr][nc] = '#'
                    q.append((nr, nc))
                    
    return count
        
        
            
    
    
def solution2():
    grid = parse_lines()

    R = len(grid)
    C = len(grid[0])
    
    low_points = []
    for r in range(R):
        for c in range(C):
            if check_low_point(grid, r, c):
                low_points.append((r, c))
                
    sizes = []
    for r, c in low_points:
        sizes.append(flood_fill(grid, r, c))
        
    sizes.sort() # To find largest 3 basins

    total = 1
    for s in sizes[-3:]:
        total *= s
    
    return total
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
