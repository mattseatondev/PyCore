from Challenges.util import pr


unsorted_list = [
    42, 17, 93, 8, 55, 61, 34, 77, 12, 5,
    88, 26, 39, 71, 3, 90, 11, 67, 50, 81
]

def merge_sort(unsorted, iters=0):
    if len(unsorted) < 2:
        return unsorted
    mid = len(unsorted) // 2
    left = merge_sort(unsorted[:mid])
    right = merge_sort(unsorted[mid:])
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
        iters += 1
    sorted_list.extend(left)
    sorted_list.extend(right)
    print(f"Iteration {iters} - Sorted list length is {len(sorted_list)}")
    return sorted_list
    
    
pr(merge_sort(unsorted_list))