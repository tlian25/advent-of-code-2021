# Day 14. Extended Polymerization 
# https://adventofcode.com/2021/day/14

from collections import Counter, defaultdict
from util.input_util import read_input_file

def parse_lines():
    lines = read_input_file(14)

    template = lines[0]
    insertions = {}
    for l in lines[2:]:
        pattern, letter = l.split(' -> ')
        insertions[pattern] = letter
        
    return template, insertions
    

def insert(template, insertions):
    newtemplate = ''
    
    for i in range(len(template)-1):
        pattern = template[i:i+2]
        newtemplate += pattern[0]
        if pattern in insertions:
            newtemplate += insertions[pattern]

    # last letter
    newtemplate += template[-1]
    return newtemplate


def score(template):
    # Most frequent count - least frequent count
    counts = Counter(list(template))
    
    maxcount = max([c for _, c in counts.items()])
    mincount = min([c for _, c in counts.items()])
    
    return maxcount - mincount



def run_steps2(template, insertions, steps):
    
    for i in range(steps):
        print(i, len(template))
        template = insert(template, insertions)

    return template



def solution1():
    template, insertions = parse_lines()
    
    STEP = 10
    template = run_steps2(template, insertions, STEP)
        
    return score(template)        
        



def solution2():
    template, insertions = parse_lines()
    
    pairs = defaultdict(int)
    counts = defaultdict(int)
    
    for i in range(len(template)-1):
        counts[template[i]] += 1
        p = template[i:i+2]
        pairs[p] += 1
    
    counts[template[-1]] += 1
    
    STEPS = 40
    
    for i in range(STEPS):
        
        newpairs = defaultdict(int)
        
        for p, n in pairs.items():
            if p in insertions:
                l = insertions[p]
                counts[l] += n
                p1 = p[0] + l
                p2 = l + p[1]
                
                newpairs[p1] += n
                newpairs[p2] += n

            else:
                newpairs[p] += n

        pairs = newpairs
    
    # Count max and mins        
    print(counts)
        
    mincount = min(counts.values())
    maxcount = max(counts.values())
        
    return maxcount - mincount
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
