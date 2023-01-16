# Day 
# https://adventofcode.com/2021/day/

from util.input_util import read_input_file

DOT = '#'
SPACE = '.'

def print_grid(grid):
    s = ''
    for row in grid:
        s += ''.join(row) + '\n'
    print(s)
    

def parse_lines():
    lines = read_input_file(13)
    dots = set()
    folds = []
    R, C = 0, 0
    for l in lines:
        if 'fold' in l:
            s = l.replace('fold along ', '').split('=')
            folds.append((s[0], int(s[1])))
        elif ',' in l:
            c, r = l.split(',')
            r = int(r)
            c = int(c)
            C = max(C, c)
            R = max(R, r)
            dots.add((r, c))
    
    R += 1
    C += 1
    grid = [[SPACE for _ in range(C)] for _ in range(R)]
    
    for r in range(R+1):
        for c in range(C+1):
            if (r, c) in dots:
                grid[r][c] = DOT

    return grid, R, C, folds
            
        
def fold_up(grid, row, R, C):
    
    # Merge rows
    up = row - 1
    dn = row + 1
    while up >= 0 and dn < R:
        #print(up, grid[up])
        #print(dn, grid[dn])
        for c in range(C):
            if grid[up][c] == DOT or grid[dn][c] == DOT:
                grid[up][c] = DOT
            else:
                grid[up][c] = SPACE
        
        up -= 1
        dn += 1
        
    return grid[:row], row, C



def fold_left(grid, col, R, C):
    # Merge cols
    lt = col - 1
    rt = col + 1
    while lt >= 0 and rt < C:
        for r in range(R):
            if grid[r][lt] == DOT or grid[r][rt] == DOT:
                grid[r][lt] = DOT
            else:
                grid[r][lt] = SPACE
                
        lt -= 1
        rt += 1
        
    return [row[:col] for row in grid], R, col



def count_dots(grid, R, C):
    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == DOT:
                count += 1
    return count



def solution1():
    grid, R, C, folds = parse_lines()
    
    for dir, v in folds[0:1]:
        if dir == 'x':
            grid, R, C = fold_left(grid, v, R, C)
        else:
            grid, R, C = fold_up(grid, v, R, C)
    
    return count_dots(grid, R, C)
    
    
def solution2():
    grid, R, C, folds = parse_lines()
    
    for dir, v in folds:
        if dir == 'x':
            grid, R, C = fold_left(grid, v, R, C)
        else:
            grid, R, C = fold_up(grid, v, R, C)
    
    print_grid(grid)
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
