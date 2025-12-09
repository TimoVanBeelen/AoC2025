# Day 9
# Advent of Code
# 09-12-2025
# Timo van Beelen


import time
import math


# Global variables
FILE_NAME = "example.in"
DIR = "Day9"


# Calculate the Eucladian distance
def calc_dist(pos1_vals: str, pos2_vals: str):
    return math.sqrt((pos1_vals[0]-pos2_vals[0])**2 + (pos1_vals[1]-pos2_vals[1])**2 + (pos1_vals[2]-pos2_vals[2])**2 )


# Main func
if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"{DIR}/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()
        input_lines = [line.removesuffix('\n') for line in input_lines]