# Day 22. Reactor Reboot 
# https://adventofcode.com/2021/day/22

from util.input_util import read_input_file

ON = 1
OFF = 0

def parse_lines():
    lines = read_input_file(22)
    # (on/off, xs, xe, ys, ye, zs, ze)
    instructions = []
    for l in lines:
        ins = []
        onoff, area = l.split()
        onoff = ON if onoff == 'on' else OFF
        ins.append(onoff)
        x, y, z = area.split(',')
        for d in (x, y, z):
            d = d.split('=')[1]
            start, end = d.split('..')
            ins.append(int(start))
            ins.append(int(end))
            
        instructions.append(ins)
    return instructions


    
# 3d grid made up entirely of cubes - one cube per integer coordinate (x, y, z)
# each cube either on or off
# at start of reboot process - they are all off
# to reboot, need to set all of the cubes to either on or off by a list of reboot steps

# Each step specifies a cuboid and wehther to turn all on or off
# Ignore cubes outside of (-50, 50)

def solve(instructions):
    # Initiate grid
    grid = {}
                
    # Turn on/off - limit grid
    for offon, xs, xe, ys, ye, zs, ze in instructions:
        xs = max(xs, -50)
        xe = min(xe, 50)
        ys = max(ys, -50)
        ye = min(ye, 50)
        zs = max(zs, -50)
        ze = min(ze, 50)

        for x in range(xs, xe+1):
            for y in range(ys, ye+1):
                for z in range(zs, ze+1):
                    grid[(x,y,z)] = offon

    # Count
    return sum(grid.values())
        


class OverlapRegion:
    def __init__(self):
        self._min = 0
        self._max = 0
        self._ins = []

    def add(self, instruction):
        pass
        
    

count = 0

def solve2(instructions):
    global count

    xoverlaps = find_x_overlaps(instructions)
    for xoverlap in xoverlaps:
        yoverlaps = find_y_overlaps(xoverlap)
        for yoverlap in yoverlaps:
            zoverlaps = find_z_overlaps(yoverlap)

            # These have x, y, and z overlap
            for zoverlap in zoverlaps:
                process_z_overlap(zoverlap)

    return count



def find_x_overlaps(instructions):
    global count
    xoverlaps = []
    
    # Turn on/off - no limit
    for i, ins in enumerate(instructions):
        (offon, xs, xe, ys, ye, zs, ze) = ins

        # group all instructions by overlaps in x
        found = False
        for overlap in xoverlaps:
            for _, xs1, xe1, _, _, _, _ in overlap:
                if xs <= xe1 and xe <= xs1:
                    found = True
                    break
            
            if found: 
                break
            
        if found:
            overlap.append(ins)
        else:
            xoverlaps.append([ins])
    
    # sum any regions without overlap in x - can process immediately
    removes = []
    for i, overlap in enumerate(xoverlaps):
        if len(overlap) == 1:
            (offon, xs, xe, ys, ye, zs, ze) = overlap[0]
            removes.append(i)
            # add on counts, ignore off counts
            if offon == 1:
                count += (xe-xs+1) * (ye-ys+1) * (ze-zs+1)

    for r in removes[::-1]:
        del xoverlaps[r]
        
    return xoverlaps

        
def find_y_overlaps(xoverlap:list):
    global count
    yoverlaps = []

    for i, ins in enumerate(xoverlap):
        (offon, xs, xe, ys, ye, zs, ze) = ins
        # group all instructions by overlaps in x
        found = False
        for overlap in yoverlaps:
            for _, _, _, ys1, ye1, _, _ in overlap:
                if ys <= ye1 and ye <= ys1:
                    found = True
                    break
            if found: 
                break
            
        if found:
            overlap.append(ins)
        else:
            yoverlaps.append([ins])
            
    
     # sum any regions without overlap in y - can process immediately
    removes = []
    for i, overlap in enumerate(yoverlaps):
        if len(overlap) == 1:
            (offon, xs, xe, ys, ye, zs, ze) = overlap[0]
            removes.append(i)
            # add on counts, ignore off counts
            if offon == 1:
                count += (xe-xs+1) * (ye-ys+1) * (ze-zs+1)

    for r in removes[::-1]:
        del yoverlaps[r]
        
    return yoverlaps



def find_z_overlaps(yoverlap:list):
    global count
    zoverlaps = []

    for i, ins in enumerate(yoverlap):
        (offon, xs, xe, ys, ye, zs, ze) = ins
        # group all instructions by overlaps in x
        found = False
        for overlap in zoverlaps:
            for _, _, _, _, _, zs1, ze1 in overlap:
                if zs <= ze1 and ze <= zs1:
                    found = True
                    break
            if found: 
                break
            
        if found:
            overlap.append(ins)
        else:
            zoverlaps.append([ins])
            
    
     # sum any regions without overlap in y - can process immediately
    removes = []
    for i, overlap in enumerate(zoverlaps):
        if len(overlap) == 1:
            (offon, xs, xe, ys, ye, zs, ze) = overlap[0]
            removes.append(i)
            # add on counts, ignore off counts
            if offon == 1:
                count += (xe-xs+1) * (ye-ys+1) * (ze-zs+1)

    for r in removes[::-1]:
        del zoverlaps[r]
        
    return zoverlaps


def process_z_overlap(zoverlap):
    global count
    grid = {}

    for i, ins in enumerate(zoverlap):
        print("Instruction:", i, "of", len(zoverlap))
        (offon, xs, xe, ys, ye, zs, ze) = ins
        for x in range(xs, xe+1):
            for y in range(ys, ye+1):
                for z in range(zs, ze+1):
                    print(x, y, z, '\r', end='')
                    grid[(x,y,z)] = offon

    # Count
    count += sum(grid.values())
        


        



def solution1():
    instructions = parse_lines()
    return solve(instructions)
    
def solution2():
    global count
    instructions = parse_lines()
    solve2(instructions)
    return count
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
