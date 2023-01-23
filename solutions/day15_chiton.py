# Day 15. Chiton 
# https://adventofcode.com/2021/day/15

from heapq import heappop, heappush
from collections import deque
from util.input_util import read_input_file

DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

def parse_lines():
    lines = read_input_file(15)
    grid = []
    for l in lines:
        grid.append([int(x) for x in l])
        
    R = len(grid)
    C = len(grid[0])
    return grid, R, C


def bfs(grid, R, C):
    
    minrisk = [[float('inf') for _ in range(C)] for _ in range(R)]
    minrisk[0][0] = 0
    
    h = [(0, 0, 0)]
    
    while h:
        d, r, c = heappop(h)
        
        if r == R-1 and c == C-1:
            return d
        
        for dr, dc in DIRS:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < R and 0 <= nc < C:
                nd = grid[nr][nc] + d
                if nd < minrisk[nr][nc]:
                    minrisk[nr][nc] = nd
                    heappush(h, (nd, nr, nc))



def solution1():
    grid, R, C = parse_lines()
    minrisk = bfs(grid, R, C)
    return minrisk

def next(x, i):
    if x+i > 9:
        return (x+i) % 10 + 1
    return x+i


def extend_right(grid, R, C, n):
    for row in grid:
        orow = row.copy()
        for i in range(1, n):
            row += [next(x, i) for x in orow]
            
    return grid, R, C*n


def extend_down(grid, R, C, n):
    for i in range(1, n):
        for r in range(R):
            ncol = [next(x, i) for x in grid[r]]
            grid.append(ncol)
            
    return grid, R*n, C





    
def solution2():
    grid, R, C = parse_lines()
    
    grid, R, C = extend_right(grid, R, C, 5)
    grid, R, C = extend_down(grid, R, C, 5)
    
    minrisk = bfs(grid, R, C)
    
    return minrisk

    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
