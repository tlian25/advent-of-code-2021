# Day 17: Trick Shot 
# https://adventofcode.com/2021/day/17

from util.input_util import read_input_file

def parse_lines():
    l = read_input_file(17)[0]
    xs, ys = l.replace('target area: ', '').split(', ')
    xs = tuple(int(x) for x in xs.replace('x=', '').split('..'))
    ys = tuple(int(y) for y in ys.replace('y=', '').split('..'))
    
    return xs, ys

# Drag - x velocity decreases by 1 toward the value 0
# Gravity - y velocity decreased by 1

# Return:
# -1 if not reached
# 0 if inside range
# 1 if past range
def inside_range(x, xs):
    if x < xs[0]: return -1
    if xs[0] <= x <= xs[1]: return 0
    if x > xs[1]: return 1


def inside_area(x, y, xs, ys):
    return (inside_range(x, xs), inside_range(y, ys))


def travel_x(x, xs):
    xval = 0
    t = 0
    while x > 0:
        t += 1
        xval += x
        
        # Check if in area
        status = inside_range(xval, xs)
        if status == 0:
            return t
        elif status == 1: # too far
            return -1
        # status == -1 not reached yet so keep going

        x -=1 

    # Haven't reached, but no more x velocity
    return -2


# Find possible values of x velocity that end up in target area
def find_x_velocity_range(xs):
    
    possiblexs = []
    
    for x in range(xs[1], -1, -1):
        t = travel_x(x, xs)
        if t > -1:
            possiblexs.append((x, t))
        elif t == -2:
            break
            
    return possiblexs



def travel_y(y, ys, t):
    yval = 0
    maxy = 0
    while t > 0:
        yval += y
        maxy = max(maxy, yval)
        y -= 1
        
        status = inside_range(yval, ys)
        if status == 0:
            return maxy
        elif status == -1:
            return -1
    
    return -2


def find_max_y(ys, t):
        
    # Find y
    for y in range(-ys[0], -ys[1]-1, -1):
        maxy = travel_y(y, ys, t)
        if maxy > -1:
            return maxy

def find_possible_ys(ys, t):
    
    possibleys = [y for y in range(ys[0], -ys[0]+1)]
    return possibleys


def solution1():
    xs, ys = parse_lines()
    
    possiblexs = find_x_velocity_range(xs)    
    maxt = max([t for x, t in possiblexs])    
    return find_max_y(ys, maxt)
    

def travel_xy(x, y, xs, ys):
    xval = 0
    yval = 0
    
    while True:
        xval += x
        yval += y
        
        status = inside_area(xval, yval, xs, ys)
        if status[0] == 0 and status[1] == 0:
            return True
        elif status[0] > 0 or status[1] < 0:
            return False
        
        x = max(x-1, 0)
        y -= 1



def solution2():
    xs, ys = parse_lines()
    
    possiblexs = find_x_velocity_range(xs)
    
    count = 0
    for x, t in possiblexs:
        possibleys = find_possible_ys(ys, t)
        for y in possibleys:
            if travel_xy(x, y, xs, ys):
                count += 1
        
    return count
        
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
