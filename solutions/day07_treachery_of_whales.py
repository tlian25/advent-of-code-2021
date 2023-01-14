# Day 7. The Treachery of Whales 
# https://adventofcode.com/2021/day/7

from statistics import mean, median
from util.input_util import read_input_file



def parse_lines():
    lines = read_input_file(7)

    positions = [int(x) for x in lines[0].split(',')]
    positions.sort()
    return positions


# Each horizontal move requires 1 fuel
# Position to cost least amount of total fuel


def calculate_fuel(positions, m):
    fuel = 0
    for p in positions: 
        fuel += abs(p - m)
    return fuel 

def solution1():
    positions = parse_lines()

    mn = round(mean(positions))
    md = round(median(positions))
    
    if md > mn:
        md, mn = mn, md
    
    fuel = float('inf')
    loc = None 
    for m in range(md-1, mn+1):
        f = calculate_fuel(positions, m)
        if f < fuel:
            fuel = f
            loc = m
    
    #print(loc)
    return fuel
        

        
def calculate_fuel2(positions, m):
    fuel = 0
    for p in positions:
        n = abs(p - m)
        fuel += n * (n+1) // 2
    return fuel
    
    
def solution2():
    positions = parse_lines()

    mn = round(mean(positions))
    md = round(median(positions))
    print(mn, md)
    
    if md > mn:
        md, mn = mn, md
    
    fuel = float('inf')
    loc = None 
    for m in range(md-1, mn+1):
        f = calculate_fuel2(positions, m)
        if f < fuel:
            fuel = f
            loc = m
    
    print(loc)
    return fuel

    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
