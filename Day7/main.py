# Day 7
# Advent of Code
# 07-12-024
# Timo van Beelen


import time


# Global variables
FILE_NAME = "input.in"
DIR = "Day7"
SPLIT_CHAR = '^'


# Check the positions above for the char,
def split_upwards(matrix: list[list], inity: int, initx: int):
    row_idx = inity
    while(row_idx >= 1):
        row_idx -= 1            # Look one row higher
        sides = [matrix[row_idx][initx-1], matrix[row_idx][initx+1]]
        if SPLIT_CHAR in sides:
            return False
        if matrix[row_idx][initx] == SPLIT_CHAR:
            return True
    return False


# Main func
if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"{DIR}/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()

    # Count the total of ^ symbols
    count  = 0
    for line in input_lines:
        count += line.count("^")

    char_mat = [list(line.removesuffix('\n')) for line in input_lines]
    
    for row_idx in range(len(char_mat)):
        for char_idx in range(len(char_mat[row_idx])):
            char = char_mat[row_idx][char_idx]
            # if the char is a . or an S, we do not care
            if char != SPLIT_CHAR: continue

            # Now the char is a ^, we should check until we reach an S or ^ right above
            # If there is a ^ on one of the sides, before reaching, add to count, otherwise not
            if split_upwards(matrix=char_mat, inity=row_idx, initx=char_idx):
                count -= 1

    print("Part 1 answer: ", count)

    end_pt1 = time.time()
    print("Runtime: ", (end_pt1-start_time)*1000, " ms")        # 30.7ms, 24.3ms, 22.6ms      

    # For part 2 a map implementation will probably work better
    # Initialise a matrix with zeros
    node_matrix = [[0]*len(line) for line in input_lines] 
    node_matrix[-1] = [1 for _ in input_lines[0]]    

    for line_idx in range(len(char_mat)-2, -1, -1):
        for char_idx in range(len(char_mat[line_idx])):
            char = char_mat[line_idx][char_idx]
            if char is not SPLIT_CHAR:
                node_matrix[line_idx][char_idx] = node_matrix[line_idx+1][char_idx]
            else:
                node_matrix[line_idx][char_idx] = node_matrix[line_idx+1][char_idx-1] + node_matrix[line_idx+1][char_idx+1]

    print("Answer pt2: ", max(node_matrix[0]))

    end_pt2 = time.time()
    print("Runtime: ", (end_pt2-end_pt1)*1000, " ms")        # 25.1ms, 34.4ms, 27.9ms      
