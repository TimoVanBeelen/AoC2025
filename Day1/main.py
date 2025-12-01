# Day 1
# Advent of Code
# 01-12-024
# Timo van Beelen


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
        if line[0] == 'L': pos = (pos-int(line[1:]))%100
        else: pos = (pos+int(line[1:]))%100
        if pos == 0: zero_pos += 1
        print(pos)

    print(zero_pos)
            