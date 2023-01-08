# Day 6. Lanternfish
# https://adventofcode.com/2021/day/6

from collections import deque
from util.input_util import read_input_file


def parse_lines():
    lines = read_input_file(6)
    fishes = deque([0 for _ in range(9)])
    
    for t in lines[0].split(','):
        fishes[int(t)] += 1

    return fishes

# Each fish creates new fish once every 7 days
# Two more days for first cycle


def solution1():
    fishes = parse_lines()
    
    for day in range(80):        
        # print(f"Day {day} - {fishes}")
        
        spawn = fishes.popleft()
        fishes[6] += spawn
        fishes.append(spawn)

    return sum(fishes)

    
def solution2():
    fishes = parse_lines()
    

    for day in range(256):
        # print(f"Day {day} - {fishes}")
        
        spawn = fishes.popleft()
        fishes[6] += spawn
        fishes.append(spawn)
        
    return sum(fishes)

    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
