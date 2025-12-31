import sys

def binary_exp(base:int, exp:int) -> int:
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
        print(exp, result, base)
    return result

print(binary_exp(int(sys.argv[1]), int(sys.argv[2])))

"""
    b = 9
    e = 4
    r = 1
    
    b = 81
    e = 2
    r = 1
    
    b = 6561
    e = 1
    r = 1
    
    r = 6561
    b = ?
    e = 0
    
    answer = 6561
"""