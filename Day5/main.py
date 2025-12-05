# Day 5
# Advent of Code
# 05-12-024
# Timo van Beelen


import time


# Global variables
FILE_NAME = "input.in"


# Main func
if __name__ == "__main__":

    start_time = time.time()      # Start timer  

    # Read the input file
    with open(f"Day5/{FILE_NAME}", "r") as file:
        input_lines = file.readlines()
        input_lines = [line.strip('\n') for line in input_lines]

    starts = []                 # A list containing the start of ID ranges
    ends = []                   # A list containing the end of ID ranges
    for line in input_lines:
        if line == '': break
        section = [int(s) for s in line.split('-')]         # Section[0] is the start of the range, section[1] is the end

        starts.append(section[0])
        ends.append(section[1])

    # Check the items if they are fresh or not
    fresh_items = 0
    for line in input_lines:
        if '-' in line or line == '': continue
        
        for i in range(len(starts)):
            if int(line) >= starts[i] and int(line) <= ends[i]:
                fresh_items += 1
                break
    
    print("Answer pt1: ", fresh_items)

    pt1_time = time.time()
    print("Part 1 cost " + str((pt1_time-start_time)*1000) + " ms")       # Duration in 3 runs: 45.5 ms, 46.9 ms, 42,4 ms


    # Part 2: take the difference of each unique range and add 1

    starts = []                 # A list containing the start of ID ranges
    ends = []                   # A list containing the end of ID ranges
    for line in input_lines:
        if line == '': break
        section = [int(s) for s in line.split('-')]         # Section[0] is the start of the range, section[1] is the end

        starts.append(section[0])
        ends.append(section[1])

    # Move the ranges to tuples and sort the ranges
    sections = []
    for i in range(len(starts)):
        t = (starts[i], ends[i])
        sections.append(t)
    sections = sorted(sections, key=lambda tup: tup[0])
    starts = [sections[i][0] for i in range(len(sections))]
    ends = [sections[i][1] for i in range(len(sections))]

    # Clean up
    change = True
    while (change):
        change = False
        for i in range(1, len(starts)):
            # Remove if not unique
            if starts[i] == starts[i-1] and ends[i] == ends[i-1]:
                starts.pop(i)
                ends.pop(i)
                change = True
                break
            # If begin is within last range
            if starts[i] <= ends[i-1]:
                # If end is outside range
                if ends[i] > ends[i-1]:
                    ends[i-1] = ends[i]
                # Always pop out this range
                starts.pop(i)
                ends.pop(i)
                change = True
                break


    result = sum([ends[i]-starts[i] for i in range(len(starts))]) + len(starts)
    print(result)

    print("Part 2 cost " + str((time.time()-start_time)*1000) + " ms")  # 3 runs: 49.5 ms, 52.7 ms, 48.0 ms
        