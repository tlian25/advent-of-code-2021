# Day 16. Packet Decoder
# https://adventofcode.com/2021/day/16

import operator
from functools import reduce
from util.input_util import read_input_file


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

DIGIT = 'DIGIT'
OPER = 'OPER'
VERSION_SUM = 0


def parse_literal(i, j, packet):
    # print("Parsing literal: ", i, j, packet[i:j])
    # literal
    num = ''
    while i < j: 
        indicator = packet[i]
        # print(packet[i:i+5])
        num += packet[i+1:i+5]
        i += 5
        if indicator == '0':
            break
    
    num = int(num, 2)
    print("Literal:", num, i)
    return num, i


def prod(l):
    i = 1
    for n in l:
        i *= n
    return i


def parse_packet(i, j, packet):
    global VERSION_SUM

    while i < j:
        curr_version = int(packet[i:i+3], 2)
        print("Version:", curr_version)
        VERSION_SUM += curr_version
        i += 3
        # read next 3
        curr_type = int(packet[i:i+3], 2)
        print("Type:", curr_type)
        i += 3
            
        if curr_type == 4:
            num, i = parse_literal(i, j, packet)
            return num, i
            
        else: 
            # operator based on type
            # find length
            operator = curr_type
            print("Operator:", curr_type)
            type_id = int(packet[i])
            i += 1
            
            nums = []
            if type_id == 0: # next 15 bits are a number that represent total length in bits
                l = int(packet[i:i+15], 2)
                i += 15
                end = i + l
                while i < end:
                    num, i = parse_packet(i, end, packet)
                    nums.append(num)
                
            elif type_id == 1: # next 11 bits
                l = int(packet[i:i+11], 2)
                i += 11
                for _ in range(l):
                    num, i = parse_packet(i, j, packet)
                    nums.append(num)
            else:
                raise ValueError("unknown type: ", type_id)
                
            # Operator
            # print("nums:", nums)
            if operator == 0:
                res = sum(nums)
            elif operator == 1:
                res = prod(nums)
            elif operator == 2:
                res = min(nums)
            elif operator == 3:
                res = max(nums)
            elif operator == 5:
                res = 1 if nums[0] > nums[1] else 0
            elif operator == 6:
                res = 1 if nums[1] > nums[0] else 0
            elif operator == 7:
                res = 1 if nums[0] == nums[1] else 0
        
            return res, i



def solution1():
    global VERSION_SUM
    packet = parse_lines()
    parse_packet(0, len(packet), packet)
    return VERSION_SUM
    

def solution2():
    packet = parse_lines()
    return parse_packet(0, len(packet), packet)[0]
    
    
    
if __name__ == '__main__':
    print("Packet Version Sum:", solution1())
    
    print('--------------')
    
    print("Packet Value:", solution2())
