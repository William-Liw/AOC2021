#!/usr/bin/env/python3
#Day 2: adventofcode.com
#calculate the horizontal position and depth of the submarine from the command inputs
#WL
# 11.01.2022
import sys

def main():
    part_one()
    part_two()

def part_one():
    print('PART ONE:')
    horiz_pos, depth = 0, 0
    afile = open('./day2Data.txt', 'r')
    for num, line in enumerate (afile, 1):
        value = int(line.split(' ')[-1])
        # check keywords and increment accordingly
        if line.startswith('forward'):
            horiz_pos += value
        elif line.startswith('up'):
            depth -= value
        elif line.startswith('down'):
            depth += value
        else:
           sys.exit(f'''The input {line.split(' ')[0]} at line {num} in the data\
            file is not a valid command''')

    print('The horizontal position is: ', horiz_pos)
    print('The depth is: ', depth)
    print('The multiplication of the 2 is: ', horiz_pos*depth)


def part_two():
    print("PART TWO:")
    horiz_pos, depth, aim = 0, 0, 0
    afile = open('./day2Data.txt', 'r')
    for num, line in enumerate (afile, 1):
        value = int(line.split(' ')[-1])
        # check keywords and increment accordingly
        if line.startswith('forward'):
            depth += value*aim
            horiz_pos += value
        elif line.startswith('up'):
            aim -= value
        elif line.startswith('down'):
            aim += value
        else:
           sys.exit(f'''The input {line.split(' ')[0]} at line {num} in the data\
            file is not a valid command''')            

    print('The horizontal position is: ', horiz_pos)
    print('The depth is: ', depth)
    print('The multiplication of the 2 is: ', horiz_pos*depth)


if __name__ == '__main__': main()
if __name__ == '__main__': main()