# Day 21. Dirac Dice
# https://adventofcode.com/2021/day/21

from collections import deque, defaultdict
from itertools import product 
from util.input_util import read_input_file


class DeterministicDice:
    def __init__(self, sides):
        self._i = -1
        self._n = sides
        self._sides = [i+1 for i in range(sides)]
        
    def roll(self) -> int:
        self._i = (self._i + 3) % self._n
        #print("Roll: ", self._sides[self._i-2], self._sides[self._i-1], self._sides[self._i])
        return self._sides[self._i-2] + self._sides[self._i-1] + self._sides[self._i] 



SIDES = [i+1 for i in range(3)]

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

SCORE_LIMIT = 1000

def solution1():
    p1, p2 = parse_lines()
    dice = DeterministicDice(100)
    
    s1, s2 = 0, 0
    
    for i in range(1, 500000):
        steps = dice.roll()
        if i % 2: # p2 turn
            p1 = (p1 + steps) % 10
            s1 += p1 + 1
    
        else: # p2 turn
            p2 = (p2 + steps) % 10
            s2 += p2 + 1
            
        # Check if Game Ends
        if s1 >= SCORE_LIMIT:
            return s2 * i * 3
            
        elif s2 >= SCORE_LIMIT:
            return s1 * i * 3
            

def createWays2steps() -> dict:
    ways2steps = defaultdict(int)
    for a, b, c in product([1, 2, 3], repeat=3):
        ways2steps[a+b+c] += 1
    return ways2steps
        
    
    
def solution2():
    p1, p2 = parse_lines()
    p1wins, p2wins = 0, 0
    ways2steps = createWays2steps()

    # p1, p2, s1, s2, isPlayerOne turn, ways to get to state
    outcomes = deque([(p1, p2, 0, 0, True, 1)])
    while outcomes:
        print(f"\rQueue length: {len(outcomes)}", end='')
        # Check if there's a winner
        p1, p2, s1, s2, p1turn, ways = outcomes.popleft()

        if s1 >= 21:
            p1wins += ways
        elif s2 >= 21:
            p2wins += ways
        else:
            # Roll Dirac dice. Add all possible outcomes back into queue
            for steps, w in ways2steps.items():
                _p1, _p2, _s1, _s2 = p1, p2, s1, s2
                if p1turn: # p1 turn
                    _p1 = (p1 + steps) % 10
                    _s1 += _p1 + 1
        
                else: # p2 turn
                    _p2 = (p2 + steps) % 10
                    _s2 += _p2 + 1

                outcomes.append((_p1, _p2, _s1, _s2, not p1turn, ways * w))
    
    print()
    print(f"P1 wins: {p1wins} - P2 wins: {p2wins}")
    return max(p1wins, p2wins)
    
    

    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
