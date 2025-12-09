# Day 4
# Advent of Code
# 04-12-2025
# Timo van Beelen


import time


# Global variables
FILE_NAME = "input.in"
PAPER = "@"
MAX_AROUND = 4


# Disgusting "pythonic" way to count number of matched objects in matrix
def find_in_matrix(matrix: list[list], obj: str):
    return len([c for r in matrix for c in r if c == obj])


if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"Day4/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()
        input_lines = [list(line.strip('\n')) for line in input_lines]

    # Set playing field size
    ROWS = len(input_lines)
    COLS = len(input_lines[0])

    # Create the search field using an extra border of .
    field = [['.']*(COLS+2) for _ in range(ROWS+2)]
    for row in range(ROWS):
        for col in range(COLS):
            if input_lines[row][col] == '@':
                field[row+1][col+1] = '@'
    
    # Go through the playing field
    accessible = 0
    for row in range(ROWS):
        for col in range(COLS):
            if input_lines[row][col] == '.': continue
            
            # Set the fields to check for paper
            check_fields = [field[row][col:col+3], field[row+1][col:col+3], field[row+2][col:col+3]]
            paper = find_in_matrix(check_fields, PAPER)
            if paper-1 < MAX_AROUND: accessible += 1            # Do not count the paperstack itself in the surroundings

    print("Answer pt1: ", accessible)

    part1_end_time = time.time()
    print("Elapsed time part 1: " + str((part1_end_time-start_time)*1000) + " ms")         # 27.9 ms

    ## Part 2: same setup, now recursive

    accessible = 1
    new_accessible = 0
    while (new_accessible != accessible):
        accessible = new_accessible
        for row in range(ROWS):
            for col in range(COLS):
                if input_lines[row][col] == '.': continue
                
                # Set the fields to check for paper
                check_fields = [field[row][col:col+3], field[row+1][col:col+3], field[row+2][col:col+3]]
                paper = find_in_matrix(check_fields, PAPER)
                if paper-1 < MAX_AROUND: 
                    new_accessible += 1            # Do not count the paperstack itself in the surroundings
                    input_lines[row][col] = "."
                    field[row+1][col+1] = "."
        
    print("Part 2: ", accessible)

    print("Elapsed time part 2: " + str((time.time()-part1_end_time)*1000) + " ms")         # 271 ms