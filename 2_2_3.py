#!/usr/bin/env python3

import sys

elements = [sys.argv[1], sys.argv[2]]
elements = [x.split('\\n') for x in elements]
elements = [[x.split(' ') for x in y] for y in elements]
elements = [[[complex(y) for y in x] for x in y] for y in elements]
elements[1] = elements[1][0]

matrix_result = []
for k in range(len(elements[0])):
    entry_value = 0
    for h in range(len(elements[0][0])):
        entry_value += elements[0][k][h] * elements[1][h]

    matrix_result.append(entry_value)



for matrix in [{'A': elements[0]}, {'B': elements[1]}, {'Result': matrix_result}]:
    for key in matrix:
        print(f'{key}:')
        for row in matrix[key]:
            print(row)

        print()
