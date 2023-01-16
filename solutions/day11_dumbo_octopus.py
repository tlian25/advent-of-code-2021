# Day 11. Dumbo Octopus
# https://adventofcode.com/2021/day/11

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(11)
    grid = []
    for l in lines:
        grid.append([int(x) for x in l])
        
    R = len(grid)
    C = len(grid[0])
    return grid, R, C 

ADJACENT = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
FLASH = '#'

# Step - increase energy level by 1
# Any octopus with energy level greater than 9 flashes
# Increases all adjacent octopuses by 1
def increment(grid, R, C):
    for r in range(R):
        for c in range(C):
            grid[r][c] += 1


def find_flashes(grid, R, C):
    # Any position that is greater than 9 will flash
    # If no positions found, then stop
    # Recursive to capture all flashes
    flashes = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] != FLASH and grid[r][c] > 9:
                # Flash and increment all adjacent
                grid[r][c] = FLASH
                flashes += 1
                for dr, dc in ADJACENT:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != FLASH:
                        grid[nr][nc] += 1


    if flashes:
        return flashes + find_flashes(grid, R, C)
    return flashes
            
    
    
def flash(grid, R, C):
    # Flash all marked octopus and reset to 0 energy
    for r in range(R):
        for c in range(C):
            if grid[r][c] == FLASH:
                grid[r][c] = 0
                
    


def solution1():
    grid, R, C = parse_lines()
    
    flashes = 0
    for _ in range(100):
        increment(grid, R, C)
        f = find_flashes(grid, R, C)
        flashes += f
        flash(grid, R, C)
        
    return flashes
    
    
def solution2():
    grid, R, C = parse_lines()
    
    step = 1
    while True:
        increment(grid, R, C)
        f = find_flashes(grid, R, C)
        # print(f"Step: {step} - {f}")

        if f == 100:
            return step
        
        flash(grid, R, C)
        step += 1
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
