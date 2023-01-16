# Day 12. Passage Pathing
# https://adventofcode.com/2021/day/12

from collections import deque, defaultdict
from util.input_util import read_input_file

# Bi-Directional graph
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        
    def __str__(self):
        return f'{self.name} - {list(self.neighbors.keys())}'
    
    def __repr__(self):
        return self.__str__()

def parse_lines():
    lines = read_input_file(12)
    nodes = {}
    for l in lines:
        n1, n2 = l.split('-')
        if n1 not in nodes:
            nodes[n1] = Node(n1)
        if n2 not in nodes:
            nodes[n2] = Node(n2)
        
        nodes[n1].neighbors[n2] = nodes[n2]
        nodes[n2].neighbors[n1] = nodes[n1]

    return nodes

# BIG caves any number of times
# Small caves once
# BFS solution

def is_lower(letter):
    return letter == letter.lower()


def bfs1(nodes):
    # current node, path order, seen
    q = deque([('start', ['start'], {'start'})])
    seen = set()
    paths = []
    
    while q:
        n, path, seen = q.popleft()
        
        if n == 'end':
            paths.append(path)
            continue
        
        if is_lower(n):
            seen.add(n)
        
        for nbr in nodes[n].neighbors:
            if nbr in seen: # start and previous lowercase
                continue
            
            new_path = path.copy()
            new_path.append(nbr)
            new_seen = seen.copy()

            q.append((nbr, new_path, new_seen))
            
    return paths
            

def solution1():
    nodes = parse_lines()
    paths = bfs1(nodes)

    return len(paths)
    

def bfs2(nodes):
    # current node, path order, seen
    q = deque([('start', ['start'], set(), False)])
    seen = set()
    paths = []
    
    while q:
        n, path, seen, twice = q.popleft()
        
        if n == 'end':
            paths.append(path)
            continue
                   
        if is_lower(n):
            seen.add(n)
            
        for nbr in nodes[n].neighbors:
            if nbr == 'start':
                continue
            
            new_twice = twice
            if nbr in seen:
                if twice:
                    continue
                else:
                    new_twice = True

            new_path = path.copy()
            new_path.append(nbr)
            new_seen = seen.copy()


            q.append((nbr, new_path, new_seen, new_twice))
            
    return paths
    
    
def solution2():
    nodes = parse_lines()
    paths = bfs2(nodes)

    return len(paths)
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
