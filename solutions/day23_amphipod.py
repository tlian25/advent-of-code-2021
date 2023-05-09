# Day 23. Amphipod
# https://adventofcode.com/2021/day/23

import heapq
from collections import deque
from copy import deepcopy
from util.input_util import read_input_file_part


def parse_lines(part:int):
    lines = read_input_file_part(23, part)
    grid = [list(l) for l in lines]
    return grid


def print_grid(grid):
    for r in grid:
        print(r)

DELIMITER = '|'

def encode(grid) -> str:
    s = ""
    for r in grid:
        s += ''.join(r) + DELIMITER
    return s[:-1]


def decode(s) -> list:
    grid = [list(x) for x in s.split(DELIMITER)]
    return grid
    
def swap(grid, r1, c1, r2, c2):
    grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

# Amphipod types
A, B, C, D = 'A', 'B', 'C', 'D'
Z = 'Z' # Fixed
WALL, SPACE = '#', '.'
# Store each state as an encoding and calculate min amount of energy to get to that state
ENERGY = {A: 1, B: 10, C: 100, D: 1000}
COLS = 11
SLOTS = (2, 4, 6, 8)
SLOT_FOR_LETTER = {A: 2, B: 4, C: 6, D: 8}


def run(grid, endstate):
    STATE = {}
    s = encode(grid)
    rows = len(grid)
    h = [(0, encode(grid))]
    
    while h:
        print(f"\rHeap size: {len(h)}", end="")
        score, s = heapq.heappop(h)
        if s in STATE and STATE[s] <= score:
            continue # already got to this state with a cheaper method
        
        STATE[s] = score
        if s == endstate:
            break
        
        grid = decode(s)
        # Process any fixed items
        #process_fixed(grid)
        
        # Row 0 - top row. Try to move any pieces back into slots
        process_top_row(h, grid, score)
        
        # Process other rows
        for row in range(1, rows):
            process_row(h, grid, row, score)

    print()
    #for s in STATE:
    #    print(s, STATE[s])
    return STATE[endstate]



def drop_in_slot(ngrid, nscore, slot, c):
    v = ngrid[0][c]
    for r in range(len(ngrid)-1, 0, -1):
        if ngrid[r][slot] == SPACE:
            swap(ngrid, r, slot, 0, c)
            nscore += r * ENERGY[v]
            return nscore


def process_fixed(grid):
    for r in range(len(grid)-1, 0, -1):
        for c in SLOTS:
            v = grid[r][c]
            if v not in (Z, SPACE):
                if SLOT_FOR_LETTER[v] == c:
                    if r == len(grid)-1 or grid[r+1][c] == Z:
                        grid[r][c] = Z # Fix item


def process_top_row(h, grid, score):
    for c in range(COLS):
        v = grid[0][c]
        if v != SPACE:
            # Move left and right as far as possible and see if can drop down into a col
            # left
            l, r = c-1, c+1
            while l >= 0:
                if grid[0][l] != SPACE:
                    break
                elif l == SLOT_FOR_LETTER[v] and grid[1][l] == SPACE and all([grid[x][l] in (v, SPACE) for x in range(2, len(grid))]):
                    ngrid = deepcopy(grid)
                    nscore = abs(c-l) * ENERGY[v] + score
                    nscore = drop_in_slot(ngrid, nscore, l, c)
                    heapq.heappush(h, (nscore, encode(ngrid)))
                l -= 1

            # right
            while r < COLS:
                if grid[0][r] != SPACE:
                    break
                elif r == SLOT_FOR_LETTER[v] and grid[1][r] == SPACE and all([grid[x][r] in (v, SPACE) for x in range(2, len(grid))]):
                    ngrid = deepcopy(grid)
                    nscore = abs(c-r) * ENERGY[v] + score
                    nscore = drop_in_slot(ngrid, nscore, r, c)
                    heapq.heappush(h, (nscore, encode(ngrid)))
                r += 1


def process_row(h, grid, row, score):
    for c in SLOTS:
        v = grid[row][c]
        # If space or blocked from above
        if v == SPACE or grid[row-1][c] != SPACE:
            continue
        
        # Only move if anything below is not in the right slot
        shouldMove = False
        for i in range(row, len(grid)):
            if SLOT_FOR_LETTER[grid[i][c]] != c:
                shouldMove = True

        if not shouldMove:
            continue

        l, r = c-1, c+1
        # Check move out left
        while l >= 0:
            if grid[0][l] != SPACE:
                break
            elif l != SLOT_FOR_LETTER[v] and l in SLOTS:
                pass # Don't land on top of slots
            else:
                ngrid = deepcopy(grid)
                nscore = (abs(c-l) + row) * ENERGY[v] + score
                swap(ngrid, row, c, 0, l)
                heapq.heappush(h, (nscore, encode(ngrid)))
            l -= 1
            
        # Check move out right
        while r < COLS:
            if grid[0][r] != SPACE:
                break
            elif r != SLOT_FOR_LETTER[v] and r in SLOTS:
                pass # Don't land on top of slots
            else:
                ngrid = deepcopy(grid)
                nscore = (abs(c-r) + row) * ENERGY[v] + score
                swap(ngrid, row, c, 0, r)
                heapq.heappush(h, (nscore, encode(ngrid)))
            r += 1


def solution1():
    grid = parse_lines(1)
    ENDSTATE = '...........|##A#B#C#D##|##A#B#C#D##'
    #ENDSTATE = '...........|##Z#Z#Z#Z##|##Z#Z#Z#Z##'
    score = run(grid, ENDSTATE)
    return score


def solution2():
    grid = parse_lines(2)
    ENDSTATE = '...........|##A#B#C#D##|##A#B#C#D##|##A#B#C#D##|##A#B#C#D##'
    score = run(grid, ENDSTATE)
    return score


if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
