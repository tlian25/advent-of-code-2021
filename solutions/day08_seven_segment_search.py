# Day 8. Seven Segment Search 
# https://adventofcode.com/2021/day/8

from collections import defaultdict
from util.input_util import read_input_file

# Segments for each digit
'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''

class Digit:
    def __init__(self):
        self.slots = [None, None, None, None, ]

 
DIGIT_TO_SEGMENTS = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

SEGMENTS_TO_DIGIT = defaultdict(list)

for n, s in DIGIT_TO_SEGMENTS.items():
    SEGMENTS_TO_DIGIT[s].append(n)

print(SEGMENTS_TO_DIGIT)

def parse_lines():
    lines = read_input_file(8)
    
    signals = []
    outputs = []
    
    for l in lines:
        s, o = l.split(' | ')
        s = s.split(' ')
        o = o.split(' ')
        signals.append(s)
        outputs.append(o)

    # print(signals)
    # print(outputs)
    return signals, outputs

def solution1():
    signals, outputs = parse_lines()
    
    count = 0
    for o in outputs:
        for d in o:
            # print(d)
            l = len(d)
            if len(SEGMENTS_TO_DIGIT[l]) == 1:
                count += 1
            
    return count


def map_digits(signal:list):
    # First map uniques - 1, 4, 7, 8
    for s in signal:
        # print(s)
        if len(s) == 2:
            ONE = s
        elif len(s) == 4:
            FOUR = s
        elif len(s) == 3:
            SEVEN = s
        elif len(s) == 7:
            EIGHT = s
                        
    # Figure out other locations based on set differences
    # Letter correspond to default location from above
    
    # Next find 0, 3
    for s in signal:
        if len(s) == 6: # 0, 6, 9
            if (EIGHT - s).pop() not in FOUR:
                NINE = s
        elif len(s) == 5: # 2, 3, 5
            if len(ONE - s) == 0:
                THREE = s
    
    # Next find 6, 9
    for s in signal:
        if len(s) == 6 and s != NINE: # 0, 6
            if (EIGHT - s).pop() in ONE:
                SIX = s
            else:
                ZERO = s
    
    # Next find 2, 5
    for s in signal:
        if len(s) == 5 and s != THREE: # 2, 5
            if (s - THREE).pop() in FOUR:
                FIVE = s
            else:
                TWO = s
                
    mapping = {'0': ZERO, '1': ONE, '2': TWO, '3': THREE, '4': FOUR, 
               '5': FIVE, '6': SIX, '7': SEVEN, '8': EIGHT, '9': NINE}

    return mapping
    



    
def solution2():
    signals, outputs = parse_lines()
    
    total = 0
    for i in range(len(signals)):
        signal = [set(x) for x in signals[i]]
        mapping = map_digits(signal)
        
        output = [set(x) for x in outputs[i]]
        
        intstr = ''
        for o in output:
            for n, s in mapping.items():
                if o == s:
                    intstr += n
                    break
        
        total += int(intstr)
        
    return total
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
