# Day 16. Packet Decoder
# https://adventofcode.com/2021/day/16

import operator
from functools import reduce
from util.input_util import read_input_file


def parse_lines():
    lines = read_input_file(16)
    return lines[0]

hex_to_bin_map = {
    "\n" : "",
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
    }

def hex2dec(line):
    return ''.join([hex_to_bin_map[h] for h in line])

def parse_lines():
    lines = read_input_file(16)
    return hex2dec(lines[0])


op_map = {
    0 : sum,
    1 : lambda x : reduce(operator.mul, x),
    2 : min,
    3 : max,
    5 : lambda x : 1 if x[0] > x[1] else 0,
    6 : lambda x : 1 if x[0] < x[1] else 0,
    7 : lambda x : 1 if x[0] == x[1] else 0
    }

# First three bits encode packet version
# Next three bits encode packet type ID

# Type ID 4 -> literal value, single binary number
# Padded with leading zeros until length is a multiple of four bits
# Each group prefixed by a 1-bit except last group prefixed by 0-bit

# Type ID !4 -> operator that performs some calculation 
# Length type ID = 0 -> next 15 bits are a number that represents total length in bits of sub-packets
# Length type ID = 1 -> next 11 bits are a number that represent number of sub-packets

VERSION_TOTAL = 0
RESULT = []
DIGIT = 'DIGIT'
OPER = 'OPER'



def parse_packet(packet) -> list:
    
    global VERSION_TOTAL
    global RESULT
    
    if packet is None or len(packet) == 0:
        return None
    
    # Header
    version = int(packet[:3], 2)
    typeID = int(packet[3:6], 2)
    print(version, typeID, len(packet))
    VERSION_TOTAL += version
    
    if typeID == 4: # literal
        packet = parse_literal(packet[6:])
    else: # operator
        RESULT.append((OPER, typeID))
        packet = parse_operator(packet[6:])
        
    return packet
        
    


def parse_literal(packet) -> list:
    
    global RESULT

    digit = ""
    while len(packet) > 4:
        lead = packet[0]
        print("Digit", lead, packet[1:5])
        digit += packet[1:5]
        packet = packet[5:]
        
        if lead == '0': # break
            digit = int(digit, 2)
            print("Literal: ", digit)
            RESULT.append((DIGIT, digit))
            return packet
         



def parse_operator(packet) -> list:
    length_typeID = packet[0]
    if length_typeID == '0':
        subpacket_length = int(packet[1:16], 2)
        print("Subpacket length: ", subpacket_length)
        subpacket = packet[16:16+subpacket_length]
        while subpacket:
            subpacket = parse_packet(subpacket)

        return packet[16+subpacket_length:]
        
        
    elif length_typeID == '1':
        subpacket_count = int(packet[1:12], 2)
        print("Subpacket count: ", subpacket_count)
        packet = packet[12:]
        for i in range(subpacket_count):
            packet = parse_packet(packet)
            
        return packet
        
        
        
    





def solution1():
    packet = parse_lines()
    
    while packet:
        packet = parse_packet(packet)
    
    print(VERSION_TOTAL)
    print(RESULT)
    


    
    
    
def solution2():
    pass
    
    
    
if __name__ == '__main__':
    print(solution1())
    
    print('--------------')
    
    print(solution2())
