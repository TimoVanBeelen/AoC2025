# Day 9
# Advent of Code
# 09-12-2025
# Timo van Beelen


import time
import math


# Global variables
FILE_NAME = "input.in"
DIR = "Day9"


# Calculate the Eucladian distance
def calc_area(point1: list, point2: list):
    return (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)


# Main func
if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"{DIR}/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()
        input_lines = [line.removesuffix('\n') for line in input_lines]

    for i in range(len(input_lines)):
        input_lines[i] = [int(k) for k in input_lines[i].split(',')]
    
    # Maximum sized square will start with one of the outer most edges
    # max_col = max(input_lines, key=lambda x: x[0])
    # min_col = min(input_lines, key=lambda x: x[0])
    # outer_col = [point for point in input_lines if (point[0] == max_col[0] or point[0] == min_col[0])]
    
    # max_row = max(input_lines, key=lambda x: x[1])
    # min_row = min(input_lines, key=lambda x: x[1])
    # outer_row = [point for point in input_lines if (point[1] == max_row[1] or point[1] == min_row[1])]

    # # Take all unique points
    # outer_points = []
    # [outer_points.append(val) for val in (outer_row+outer_col) if val not in outer_points]

    areas = []
    for k in range(len(input_lines)):
        point = input_lines[k]
        for i in range(k, len(input_lines)):
            if input_lines[i] == point: continue
            areas.append(calc_area(point, input_lines[i]))

    print(max(areas))
    
    print("Time: ", (time.time()-start_time)*1000, " ms")