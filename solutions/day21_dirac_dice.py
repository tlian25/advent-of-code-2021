# Day 21. Dirac Dice
# https://adventofcode.com/2021/day/21

from util.input_util import read_input_file


class Dice:
    def __init__(self, sides):
        self._i = -1
        self._n = sides
        self._sides = [i+1 for i in range(sides)]
        
    def roll(self) -> int:
        self._i = (self._i + 3) % self._n
        print("Roll: ", self._sides[self._i-2], self._sides[self._i-1], self._sides[self._i])
        return self._sides[self._i-2] + self._sides[self._i-1] + self._sides[self._i] 
        
        

def parse_lines():
    lines = read_input_file(21)
    # Positions for p1 and p2
    p1 = int(lines[0].split(' ')[-1])
    p2 = int(lines[1].split(' ')[-1])
    return p1-1, p2-1

    
    
# Roll dice 3 times and add up results
# Move pawn that many times forward around track
# Increase score by value of space their pawn stopped on
# Immediately ends as win for player who reaches 1000 score

dice = Dice(100)
SCORE_LIMIT = 1000

def solution1():
    p1, p2 = parse_lines()
    
    s1, s2 = 0, 0
    
    for i in range(1, 500000):
        steps = dice.roll()
        if i % 2: # p2 turn
            p1 = (p1 + steps) % 10
            s1 += 10 if p1 == 0 else p1 + 1
    
        else: # p2 turn
            p2 = (p2 + steps) % 10
            s2 += 10 if p2 == 0 else p2 + 1
            
        print(s1, s2)
    
        # Check if Game Ends
        if s1 >= SCORE_LIMIT:
            print(i)
            return s2 * i * 3
            
        elif s2 >= SCORE_LIMIT:
            print(i)
            return s1 * i * 3
            

    
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
