# Day 3
# Advent of Code
# 03-12-024
# Timo van Beelen


import time

# Global variables
FILE_NAME = "input.in"


if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"Day3/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()

    joltage = 0

    # Go through all battery packs
    for line in input_lines:
        int_list = [int(i) for i in line.strip('\n')]       # Convert string to integer list
        val1 = max(int_list[:-1])                           # Find the maximum value that is not on the last index
        val1_idx = int_list.index(val1)                     # Find the index of this value

        int_list = int_list[val1_idx+1:]                    # Change the list to find the second value
        val2 = max(int_list)                                # Highest value in new list

        joltage += val1*10 + val2                           # Append joltage of the battery

    print(joltage)
    part1_end_time = time.time()

    print("Elapsed time part 1: " + str((part1_end_time-start_time)*1000) + " ms")         # 7.9 ms

    ## PART 2
    # Same setup, only looping with changing list size
    high_joltage = 0

    for line in input_lines:
        int_list = [int(i) for i in line.strip('\n')]       # Convert string to integer list

        joltage_list = []
        for i in range(-11, 0):
            val = max(int_list[:i])
            val_idx = int_list.index(val)
            int_list = int_list[val_idx+1:]
            joltage_list.append(val)

        last_val = max(int_list)
        joltage_list.append(last_val)
        high_joltage += int(''.join([str(s) for s in joltage_list]))
    
    print("Part 2 result: " + str(high_joltage))

    print("Elapsed time: " + str((time.time()-part1_end_time)*1000) + " ms")            # 5.3 ms, blijkbaar duurt lezen van bestanden lang
        
        