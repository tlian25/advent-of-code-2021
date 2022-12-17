# Day 4. Giant Squid 
# https://adventofcode.com/2021/day/4

from util.input_util import read_input_file

def parse_row(row):
    r = []
    for i in range(0, len(row), 3):
        r.append(int(row[i:i+2]))
    return r
        

def parse_lines():
    lines = read_input_file(4)
    nums = [int(x) for x in lines[0].split(',')]
    
    boards = []
    currboard = []
    for i in range(2, len(lines)):
        l = lines[i]
        if l == '':
            boards.append(currboard)
            currboard = []
        else:
            currboard.append(parse_row(l))
            
    boards.append(currboard)
    return nums, boards


def print_board(board):
    for b in board:
        print('\t'.join([str(x) for x in b]))



MARKED = '#'

def mark_board(board, n):
    for r in range(5):
        for c in range(5):
            if board[r][c] == n:
                board[r][c] = MARKED
                return r, c
    return None, None


def check_bingo(board, r, c):
    # check horizontal
    BINGO = True
    for i in range(5):
        if board[r][i] != MARKED:
            BINGO = False
            break
        
    if BINGO: return True

    # Check vertical
    BINGO = True
    for i in range(5):
        if board[i][c] != MARKED:
            BINGO = False
            break
    if BINGO: return True
    
    # No diagonals for this version
    return False


def get_score(board, called):
    total = 0
    for r in range(5):
        for c in range(5):
            if board[r][c] != MARKED:
                total += board[r][c]
                
    return total * called
                


def solution1():
    nums, boards = parse_lines()
        
    for n in nums:
        for b in boards:
            r, c = mark_board(b, n)
            if r is not None:
                bingo = check_bingo(b, r, c)

                if bingo:
                    #print(n, bingo)
                    #print_board(b)
                    return get_score(b, n)



def solution2():
    nums, boards = parse_lines()
    
    in_play = set(range(len(boards)))
    for n in nums:        
        for i in range(len(boards)):
            if i not in in_play:
                # Board already won and not in play
                continue
            
            b = boards[i]
            r, c = mark_board(b, n)
            if r is not None:
                bingo = check_bingo(b, r, c)
                if bingo:
                    in_play.remove(i)
                    
                    if not in_play:
                        return get_score(b, n)
                    

                    
        
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
