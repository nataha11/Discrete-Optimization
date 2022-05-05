#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from operator import attrgetter
Item = namedtuple("Item", ['index', 'value', 'weight', 'dens'])

def solve_it(input_data):

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), int(parts[0]) / int(parts[1])))

    # a DP algorithm
    
    n = len(items)
    # table of optimal knapsack values
    table = [[0 for j in range(capacity + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        if i > 0:
            cur_value = items[i - 1].value
            cur_weight = items[i - 1].weight
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                continue
            elif cur_weight > j:
                table[i][j] = table[i - 1][j]
            else:
                new_val = table[i - 1][j - cur_weight] + cur_value
                old_val = table[i - 1][j]
                table[i][j] = max(new_val, old_val)
                
    #finding the optimal solution in the table            
    cur_cap = capacity
    taken = [0]*n
    for i in reversed(range(n)):
        if table[i][cur_cap] == table[i + 1][cur_cap]:
            continue
        else:
            taken[i] = 1
            cur_cap -= items[i].weight
            
    
    # prepare the solution in the specified output format
    output_data = str(table[n][capacity]) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

