from math import inf

dataset =[
     3,   7,  12,  15,  19,  22,  27,  31,  35,  38,
    41,  44,  48,  51,  56,  59,  63,  67,  71,  74,
    78,  81,  85,  88,  92,  95,  99, 103, 107, 110,
   114, 118, 121, 125, 129, 133, 137, 141, 145, 149,
   153, 157, 161, 165, 169, 173, 177, 181, 185, 189
]

def sliding_window(lst:list[int], k:int) -> int:
    if len(lst) < k:
        raise IndexError(f'List must be of length greater than window param: {k}')
    max_sum = 0
    cur_sum = 0
    left = 0
    right = 0
    while right < len(lst):
        cur_sum += lst[right]
        if right - left + 1 < k:
            right += 1
        if right - left + 1 == k:
            if max_sum < cur_sum:
                max_sum = cur_sum
            cur_sum -= lst[left]
            left += 1
    return max_sum

print(sliding_window(dataset, 3))