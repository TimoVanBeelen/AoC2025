# Day 2
# Advent of Code
# 02-12-024
# Timo van Beelen

import math
import time
import re

# Global variables
FILE_NAME = "input.in"


# Function to increment the number string in a correct way 
def increment_numstr(numstr: str):
    if len(numstr) == 1: return str(int(numstr)+1)                                      # Catch before evaluating next if-statement
    if numstr[0] == "0" and sum([int(i) for i in numstr[1:]]) != 9*len(numstr[1:]):     # Perserve the 0 at the front if no overflow to it
        return "0" + str(int(numstr)+1)
    else:
        return str(int(numstr)+1)


# Main func
if __name__ == "__main__":

    start_time = time.time()      # Start timer          

    # Read the input file
    with open(f"Day2/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()

    # Split the line into the seperate sections
    sections = input_lines[0].split(',')
    answer = 0

    # Loop through each set
    for section in sections:
        section = [i for i in section.split('-')]               # Split the section into the starting number and end number
        if len(section[0])%2 != 0: section[0] = "0"+section[0]    # Add 0 to the front if numbers cannot be split right through the middle

        # Split the start number right through the middle
        half_size = math.floor(len(section[0])/2)
        left_half = section[0][0:half_size]
        right_half = section[0][half_size:]

        # While we are in section
        while (int(left_half+right_half)) <= int(section[1]):
            if (left_half == right_half):                                           # If both halves are equal, add to result
                if left_half[0] != "0": answer += int(left_half+right_half)         # Numbers starting with 0 should not be counted
                left_half = increment_numstr(left_half)
            elif int(left_half) < int(right_half):                                  # Increment left halve by 1 at a time
                left_half = increment_numstr(left_half)

            right_half = left_half                                                  # Right halve can never be lower than the left halve

    print(answer)           # Print the final answer to pt 1
    pt1_time = time.time()
    print("Part 1 cost " + str((pt1_time-start_time)*1000) + " ms")       # kostte 2.26 ms

    # Nu toch maar regex...
    answer2 = 0
    reg_check = re.compile(r'^(\d+)\1+$')
    for section in sections:
        # Split into start and stop value of section
        section = [int(i) for i in section.split('-')]

        for number in range(section[0], section[1]):
            if reg_check.match(str(number)):
                answer2 += number

    print(answer2)
    print("Part 2 cost " + str((time.time()-pt1_time)*1000)+" ms")        # kostte 1.2 secondes       

