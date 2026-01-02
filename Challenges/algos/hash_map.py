no_repeat = [
     3,   7,  12,  15,  19,  22,  27,  31,  35,  38,
    41,  44,  48,  51,  56,  59,  63,  67,  71,  74,
    78,  81,  85,  88,  92,  95,  99, 103, 107, 110,
   114, 118, 121, 125, 129, 133, 137, 141, 145, 149,
   153, 157, 161, 165, 169, 173, 177, 181, 185, 189
]

repeat = [
     3,   7,  12,  12, 15,  19,  22,  27,  31,  35,  38,
    41,  44,  48,  51,  56,  59,  63,  67,  71,  74,
    78,  81,  85,  88,  92,  95,  99, 103, 107, 110,
   114, 118, 121, 125, 129, 133, 137, 141, 145, 149,
   153, 157, 161, 165, 165, 169, 173, 177, 181, 185, 189, 189
]

def hash_map(numbers:list[int]) -> list[int]:
    repeated = set()
    seen = set()
    for n in numbers:
        if n in seen:
            repeated.add(n)
        else:
            seen.add(n)
    print(f"The following numbers were repeated in the list: {', '.join((str(r) for r in repeated))}")
    return list(repeated)

print(hash_map(no_repeat))
print(hash_map(repeat))