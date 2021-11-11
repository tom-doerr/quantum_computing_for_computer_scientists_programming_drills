#!/usr/bin/env python3


def addition(a, b):
    for xi in range(len(a)):
        for yi in range(len(a[0])):
            a[xi][yi][0] += b[xi][yi][0]
            a[xi][yi][1] += b[xi][yi][1]
    return a

def inverse(a):
    for xi in range(len(a)):
        for yi in range(len(a[0])):
            a[xi][yi][0] = -a[xi][yi][0]
            a[xi][yi][1] = -a[xi][yi][1]
    return a

def scalar_multiplication(s, a):
    for xi in range(len(a)):
        for yi in range(len(a[0])):
            a[xi][yi][0] *= s
            a[xi][yi][1] *= s

    return a

# test it
if __name__ == "__main__":
    a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    b = [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]
    print(addition(a, b))
    print('Expected: [[[2, 3], [4, 5]], [[6, 7], [8, 9]]]')
    a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    b = [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]
    print(inverse(a))
    print('Expected: [[[-1, -2], [-3, -4]], [[-5, -6], [-7, -8]]]')
    a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    b = [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]
    print(scalar_multiplication(2, a))
    print('Expected: [[[2, 4], [6, 8]], [[10, 12], [14, 16]]]')




