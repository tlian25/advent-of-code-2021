# Day 1. Sonar Sweep
# https://adventofcode.com/2022/day/1

from util.input_util import read_input_file

def read_measurements():
    lines = read_input_file(1)
    return [int(l) for l in lines]
        


def solution1():
    measures = read_measurements()
    inc_count = 0
    for i in range(1, len(measures)):
        if measures[i] > measures[i-1]:
            inc_count +=1
    return inc_count

    
def solution2():
    measures = read_measurements()
    inc_count = 0
    for i in range(4, len(measures)+1):
        win_curr = measures[i-3:i]
        win_prev = measures[i-4:i-1]
        if sum(win_curr) > sum(win_prev):
            inc_count += 1
        
    return inc_count
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
