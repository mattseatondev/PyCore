import pytest

def binary_exponentiation(num:int, exp:int, iters=0) -> str:
    result = 1
    while exp > 0:
        if exp % 2 != 0:
            result *= num
        num *= num
        exp //= 2
        iters += 1
    return f"Found result {result} in {iters} Iterations"

print(binary_exponentiation(5, 100))