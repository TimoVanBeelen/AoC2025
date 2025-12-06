# Day 6
# Advent of Code
# 06-12-024
# Timo van Beelen


import time


# Global variables
FILE_NAME = "input.in"
DIR = "Day6"


# Main func
if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"{DIR}/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()
        input_lines = [line.strip('\n') for line in input_lines]