# Day 20. Trench Map 
# https://adventofcode.com/2021/day/20

import copy
from util.input_util import read_input_file

LIGHT = '1'
DARK = '0'

def parse_lines():
    lines = read_input_file(20)
    algo = lines[0].replace('#', '1').replace('.', '0')
    grid = []
    
    for l in lines[2:]:
        grid.append(list(l.replace('#','1').replace('.','0')))
    
    return algo, grid


def print_grid(grid):
    for row in grid:
        print("".join(row).replace(DARK, '.').replace(LIGHT, '#'))

# Put a border of darks around the grid
def pad_grid(grid, algo, pad):
    PAD = pad
    
    # sides
    for r in range(len(grid)):
        grid[r] = [PAD for _ in range(2)] + grid[r] + [PAD for _ in range(2)]
    
    # top and bottom
    pad = [PAD for _ in range(len(grid[0]))]
    grid = [pad.copy() for _ in range(2)] + grid + [pad.copy() for _ in range(2)]
    return grid


def sharpen_image(grid, algo):
    
    newgrid = copy.deepcopy(grid)

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if r in [0, len(grid)-1] or c in [0, len(grid[0])-1]:
                newgrid[r][c] = process_edge(r, c, grid, algo)
            else:
                newgrid[r][c] = process_pixel(r, c, grid, algo)
            
    # Consider sides
    return newgrid
    
    

def process_pixel(r, c, grid, algo):
    r1 = "".join(grid[r-1][c-1:c+2])
    r2 = "".join(grid[r][c-1:c+2])
    r3 = "".join(grid[r+1][c-1:c+2])
    
    idx = int(r1+r2+r3, 2)
    return algo[idx]


def process_edge(r, c, grid, algo):
    val = grid[r][c]
    if val == LIGHT:
        return algo[-1]
    return algo[0]


def count_pixels(grid):
    count = 0
    for row in grid:
        for c in row:
            if c == LIGHT:
                count += 1
    return count


def solution1():
    algo, grid = parse_lines()
    
    for i in range(50):
        # print(i)
        # Alternate padding between light and dark
        if algo[0] == DARK:
            pad == DARK
        elif i % 2 == 0:
            pad = DARK
        else:
            pad = LIGHT
            
        grid = pad_grid(grid, algo, pad)
        grid = sharpen_image(grid, algo)
    
    #print_grid(grid)

    return count_pixels(grid)
    
    
    
    


def solution2():
    algo, grid = parse_lines()
    

    for i in range(50):
        # print(i)
        # Alternate padding between light and dark
        if algo[0] == DARK:
            pad == DARK
        elif i % 2 == 0:
            pad = DARK
        else:
            pad = LIGHT
            
        grid = pad_grid(grid, algo, pad)
        grid = sharpen_image(grid, algo)
    
    #print_grid(grid)
    
    return count_pixels(grid)
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())