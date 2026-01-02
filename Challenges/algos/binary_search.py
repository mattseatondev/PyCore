from typing import List
import pytest

from Challenges.util import pr

class SortedList(List[int]):
    def __init__(self, values):
        if values != sorted(values):
            raise ValueError(f'Must be a sorted list: {values}')
        super().__init__(values)

dataset = SortedList([
     3,   7,  12,  15,  19,  22,  27,  31,  35,  38,
    41,  44,  48,  51,  56,  59,  63,  67,  71,  74,
    78,  81,  85,  88,  92,  95,  99, 103, 107, 110,
   114, 118, 121, 125, 129, 133, 137, 141, 145, 149,
   153, 157, 161, 165, 169, 173, 177, 181, 185, 189
])


def binary_search(data:SortedList, num:int, iterations=0):
    iterations += 1
    half_len = len(data) // 2
    singulal = '' if iterations == 1 else 's'
    print(half_len, data[half_len])
    if data[half_len] == num:
        return f"Successfully found {num} in the sorted list after {iterations} iteration{singulal}!"
    if len(data) == 1:
        raise ValueError(f"Could not locate {num} in sorted list. Failed after {iterations} iteration{singulal}")
    segment = data[:half_len] if data[half_len] > num else data[half_len+1:]
    pr(segment)
    return binary_search(SortedList(segment), num, iterations)

def test_binary_search():
    fail_case = [1, 3, 5, 6, 100]
    not_sorted = [3, 1, 4, 1, 6, 9]
    assert 'Success' in binary_search(dataset, 85)
    with pytest.raises(ValueError) as excinfo:
        binary_search(SortedList(fail_case), 85)
    assert 'Could not locate' in str(excinfo.value)
    # Invalid SortedList
    with pytest.raises(ValueError) as excinfo:
        SortedList(not_sorted)
    assert 'Must be a sorted list' in str(excinfo.value)