#!/usr/bin/env/python3
#Day 1: adventofcode.com
#number of times the depth has increased
#WL
# 31.12.2021

def main():
    depths = readfile()
    part_one(depths)
    part_two(depths, 3)


def part_one(adepths):
    counter = 0
    prev_depth = adepths[0]

    for new_depth in adepths:
        if (new_depth > prev_depth):
            counter += 1
        prev_depth = new_depth
    print(counter)

def part_two(adepths, sample_size):

    #declare variables
    counter, new_sum = 0, 0
    prev_sum = sum(adepths[0: sample_size])

    for i in range(len(adepths) - (sample_size - 1)):
        #read from file and add to new_sum
        new_sum = sum(adepths[i: i + sample_size])
        #compare values and increment counter if needed
        if new_sum > prev_sum:
            counter += 1

        prev_sum = new_sum
    print(counter)

def readfile():
    afile = open('depthInput.txt', 'r')
    alist =[]
    for line in (afile):
        alist.append(int(line.rstrip()))
    return alist

if __name__ == '__main__': main()
