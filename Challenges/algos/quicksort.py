from Challenges.util import pr


unsorted_list = [
    42, 17, 93, 8, 55, 61, 34, 77, 12, 5,
    88, 26, 39, 71, 3, 90, 11, 67, 50, 81
]

def quicksort(lst:list[int], iters=0) -> list[int]:
    if len(lst) < 2:
        return lst
    pvt_index = len(lst) // 2
    pivot = lst[pvt_index]
    left = []
    right = []
    for elem in lst[:pvt_index] + lst[pvt_index + 1:]:
        if elem < pivot:
            left.append(elem)
        else:
            right.append(elem)
    sorted = quicksort(left, iters) + [pivot] + quicksort(right, iters)
    if len(sorted) == len(unsorted_list):
        print(f'Sorted the list in {iters} Iterations')
    return sorted

pr(quicksort(unsorted_list))