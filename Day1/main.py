# Day 1
# Advent of Code
# 01-12-2025
# Timo van Beelen

import math

# Global variables
FILE_NAME = "input.in"

if __name__ == "__main__":
    # Read the input file
    with open(f"Day1/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()

    pos = 50            # Initial position of dial is 50
    zero_pos = 0        # Amount of times the dial reached 0 

    for line in input_lines:
        line = line.strip('\n')

        # Check whether to move up or down in numbers and move that amount
        if line[0] == 'L': move = -1*int(line[1:])
        else: move = int(line[1:])

        # Adapt for all values larger than 100
        while abs(move) > 100:
            zero_pos +=1
            if move > 0: move -= 100
            else: move += 100
        
        if (move > 0) and (pos != 0) and ((pos+move)%100 <= pos):
            zero_pos += 1
        elif (move < 0) and (pos!= 0) and ((pos+move)%100 >= pos):
            zero_pos += 1
        elif (pos+move)%100 == 0:
            zero_pos += 1
        
        # print(zero_pos)
        pos = (pos+move)%100

    print(zero_pos)         # Too low: 3441, not correct: 5976, 4485, 6889, 6707, 7458
            