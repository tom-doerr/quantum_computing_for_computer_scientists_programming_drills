#!/usr/bin/env python3

from e2_1_1 import *
#import 

def test_211():
    for a, b, tests in [
            ((2, 1), (1, 2),
                    [
                            (addition, (3, 3)),
                            ]),
            ]:
        for function, solution in tests:
            assert function(a, b) == solution

    assert inverse((2, -1)) == (-2, 1)
    assert scalar_multiplication(3, (2, -1)) == (6, -3)
    
