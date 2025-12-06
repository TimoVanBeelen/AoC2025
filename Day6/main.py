# Day 6
# Advent of Code
# 06-12-024
# Timo van Beelen


import math
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

    # Format the matrix to split digits and operators and remove white spaces and empty strings
    split_input = [line.split(" ") for line in input_lines]
    for i in range(len(split_input)):
        arr_tmp = [item for item in split_input[i] if item != '']
        split_input[i] = arr_tmp
    
    # Transpose matrix for easier calculations
    transposed = [[] for i in split_input[0]]
    for i in range(len(split_input)):
        for j in range(len(split_input[i])):
            transposed[j].append(split_input[i][j])
        
    answers = []
    for calc in transposed:
        if calc[-1] == '+':
            answers.append(sum([int(i) for i in calc[:-1]]))
        elif calc[-1] == '-':
            answers.append(sum(-1*int(i) for i in calc[:-1]))
        elif calc[-1] == '*':
            ans = 1
            for i in calc[:-1]: ans *= int(i)
            answers.append(ans)
        else:
            print("Unknown symbol: ", calc[-1])

    print("Total sum of answers: ", sum(answers))

    end_pt1 = time.time()
    print("Time for part 1: ", (end_pt1-start_time)*1000, " ms")        # Runs: 6.5ms, 9.3ms, 5,9 ms
    
