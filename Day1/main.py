# Day 1
# Advent of Code
# 01-12-024
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

        if pos == 0:
            zero_pos += math.floor(abs(move/100))
        else:
            if (pos+move == 0) or (pos+move == 100): zero_pos += 1
            else: zero_pos += round(abs(move/100))
        pos = (pos+move)%100

    print(zero_pos)         # Too low: 3441, not correct: 5976, 4485, 6889, 6707
            