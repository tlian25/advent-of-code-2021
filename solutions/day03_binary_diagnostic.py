# Day 3. Binary Diagnostic 
# https://adventofcode.com/2021/day/3

from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(3)
    return lines



# Gamma Rate
# Epsilon Rate
# power = gamma * epsilon

def convert_to_decimal(l:list):
    n = ''.join([str(x) for x in l])
    return int(n, 2)

def solution1():
    # Sum digits in each position and round up to 1 or down to 0
    lines = parse_lines()
    L = len(lines[0]) # length of binary nums
    N = len(lines)
    sums = [0 for _ in range(L)]
    
    for l in lines:
        for i in range(L):
            sums[i] += int(l[i])
            
    gamma = [round(x / N) for x in sums]
    epsilon = [(x+1) % 2 for x in gamma]
    
    # Convert to decimal
    gamma = convert_to_decimal(gamma)
    epsilon = convert_to_decimal(epsilon)
    return gamma * epsilon
    
    
# Oxygen generator rating
# CO2 scrubber rating
# Life support rating

# Takes a list and return two lists based on most frequent digit in the first spot
def filter_lists(lines:list, index:int) -> tuple:
    ones = []
    zeros = []
    for l in lines:
        if l[index] == '1':
            ones.append(l)
        else:
            zeros.append(l)
            
    if len(ones) >= len(zeros):
        return ones, zeros
    return zeros, ones


def solution2():
    
    lines = parse_lines()
    
    oxy = lines
    i = 0
    while len(oxy) > 1:
        oxy, _ = filter_lists(oxy, i)
        i += 1
        #print(len(oxy))
        
    oxy = int(oxy[0], 2)
    #print('Oxy:', oxy)
    
    co2 = lines
    i = 0
    while len(co2) > 1:
        _, co2 = filter_lists(co2, i)
        i += 1
        #print(len(co2))
        
    co2 = int(co2[0], 2)
    #print('CO2:', co2)
    
    return oxy * co2
    
    
    
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
