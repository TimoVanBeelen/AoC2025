# Day 6.2
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
        input_lines = [list(line.strip('\n')) for line in input_lines]
    
    operators = [c for c in list(input_lines[-1]) if c != ' ']
    
    # Transpose matrix for easier calculations
    transposed = [[] for i in input_lines[0]]
    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            transposed[j].append(input_lines[i][j])

    nums = [''.join(i[:-1]) for i in transposed]
    nums = [n.replace(' ', '') for n in nums]
    
    nr_rows = len(input_lines)
    matrix = []
    row = []
    for i in nums:
        if i == '':
            row.append(operators[0])
            operators.pop(0) 
            matrix.append(row)
            row = []
            continue
        row.append(i)
    row.append(operators[0])
    matrix.append(row)
        
        
    answers = []
    for calc in matrix:
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

    end_pt2 = time.time()
    print("Time for part 2: ", (end_pt2-start_time)*1000, " ms")        # Runs: 45.1 ms, 45.9 ms, 17.0 ms