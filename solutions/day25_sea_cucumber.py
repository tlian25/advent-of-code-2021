# Day 25. Sea Cucumber
# https://adventofcode.com/2021/day/24

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(25)
    grid = [list(l) for l in lines]
    return grid

def print_grid(grid):
    s = ''
    for row in grid:
        s += ''.join(row) + '\n'
    s += '\n'
    print(s)

grid = parse_lines()
NR = len(grid)
NC = len(grid[0])

# two herds - one moves east > and one moves south v
# each location can contain at most one sea cucumber
# every step, sea cucumbers attempt to move forward one location simultaenously
# see if next slot is open
# east herd moves first, then south herd move
# wrap around grid
# iterate until no sea cucumbers move


EMPTY = '.'
EAST = '>'
SOUTH = 'v'



def move_east():
    moves = []
    # Examine first
    for r in range(NR):
        for c in range(NC):
            if grid[r][c] == EAST:
                nc = (c+1) % NC
                if grid[r][nc] == EMPTY:
                    moves.append((r, c, nc))
                    
    for r, c, nc in moves:
        grid[r][c] = EMPTY
        grid[r][nc] = EAST
    
    return len(moves)
                    

def move_south():
    moves = []
    # Examine first
    for r in range(NR):
        for c in range(NC):
            if grid[r][c] == SOUTH:
                nr = (r+1) % NR
                if grid[nr][c] == EMPTY:
                    moves.append((r, c, nr))
                    
    for r, c, nr in moves:
        grid[r][c] = EMPTY
        grid[nr][c] = SOUTH
        
    return len(moves)
                


def step():
    eastmoves = move_east()
    southmoves = move_south()
    
    steps = 1
    while eastmoves + southmoves > 0:
        steps += 1
        print(f'{steps}\r', end = '')
        eastmoves = move_east()
        southmoves = move_south()

    return steps


def solution1():
    return step()
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
