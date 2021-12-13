#!/usr/bin/env python3

import sys

matrices = [sys.argv[1], sys.argv[2]]
matrices = [x.split('\\n') for x in matrices]
matrices = [[x.split(' ') for x in y] for y in matrices]
matrices = [[[complex(y) for y in x] for x in y] for y in matrices]

matrix_result = []
for k in range(len(matrices[0])):
    row = []
    for j in range(len(matrices[1][0])):
        entry_value = 0
        for h in range(len(matrices[0][0])):
            entry_value += matrices[0][k][h] * matrices[1][h][j]

        row.append(entry_value)

    matrix_result.append(row)


for matrix in [{'A': matrices[0]}, {'B': matrices[1]}, {'Result': matrix_result}]:
    for key in matrix:
        print(f'{key}:')
        for row in matrix[key]:
            for entry in row:
                print(entry, end=' ')
            print()

        print()
