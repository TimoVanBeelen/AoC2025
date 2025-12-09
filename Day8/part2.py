# Day 8, part 2
# Advent of Code
# 08-12-024
# Timo van Beelen


import time
import math


# Global variables
FILE_NAME = "input.in"
DIR = "Day8"


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
        
    for i in range(len(input_lines)):
        input_lines[i] = [int(k) for k in input_lines[i].split(',')]
    
    # Create an array with the distance between all points
    distances = []
    for i in range(len(input_lines)):
        for j in range(i+1, len(input_lines)):
            # Append to array, the index is the ID of a point
            distances.append([calc_dist(input_lines[i], input_lines[j]), i, j])

    made_connections = 0
    circuits = [[idx] for idx in range(len(input_lines))]
    last_x = []
    while (True):
        print("Remaining single circuits: ", len(circuits))
        # Find the new shortest path and remove from the distances
        new_connection = min(distances, key=lambda x: x[0])
        distances.pop(distances.index(new_connection))
        
        # 
        i1 = -1
        i2 = -1

        # Map the correct circuits
        for i, val in enumerate(circuits):
            # Check if there is a circuit with the index
            if new_connection[1] in val:
                i1 = i
            if new_connection[2] in val:
                i2 = i

        if i1 != i2:
            circuits[i1].extend(circuits[i2])
            del circuits[i2]

        if len(circuits) == 1:
            last_x = [input_lines[new_connection[1]][0], input_lines[new_connection[2]][0]]
            break
        
        # New connection, yay
        made_connections += 1

    print("Answer part 2: ", last_x[0]*last_x[1])

    print("Time: ", (time.time()-start_time)*1000, " ms")           # 40 sec, ripppp
