import sys
from functools import cache
from typing import Optional

# Write a function that returns the nth FN

def fib_nth(n:int) -> int:
    # Track cur and next values
    c, x = 0, 1
    # Add ctr, use in while loop (while ctr < n)
    ctr = 0
    while ctr < n:
    # On each iteration, increment prev by cur, set cur to prev
        c, x = x, c + x
        ctr += 1
    # When ctr == n: return cur
    return c

# print(fib_nth(int(sys.argv[1])))

def fib_even_sum(n:int) -> int:
    ctr = 0
    c, x = 0, 1
    even_sum = 0
    while ctr < n:
        c, x = x, c + x
        if not c % 2:
            even_sum += c
        ctr += 1
    return even_sum

# print(fib_even_sum(int(sys.argv[2])))

# In the event of a large n value, uses cache to create memoized value of fnc result
@cache    
def fib_rcrs(n:int) -> int:
    # Create a binary tree with bottom/return values as 1 and 0
    if n in (0, 1):
        return n
    # Fib Seq numbers are always equal the sum of fib[n - 1] + fib[n + 2]
    return fib_rcrs(n - 1) + fib_rcrs(n - 2)

def fib_nth_rcrs(n:int) -> int:
    if n in (0, 1):
        return n
    return fib_nth_rcrs(n - 1) + fib_nth_rcrs(n - 2)

# print(fib_nth_rcrs(int(sys.argv[3])))

# class TreeNode:
#     # Note forward reference here: TreeNode not fully intialized, so 'TreeNode' hint used in Optional
#     def __init__(self, val:int, left:Optional['TreeNode']=None, right:Optional['TreeNode']=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
#     def sum_as_root(self):
#         l = 0 if not self.left else self.left.val
#         r = 0 if not self.right else self.right.val
#         return self.val + l + r
    
#     def extract_vals(self):
#         return self.val + (0 if not self.left else self.left.val) + (0 if not self.right else self.right.val)

# @cache
# def tree_path_sum(root:TreeNode, target:int) -> list[list[int]]:
#     children = (0 if not node else node for node in (root.left, root.right))
#     if all(not child for child in children):
#         return output
#     for child in children:
#         if isinstance(child, TreeNode):
#             child_sum = child.sum_as_root()
#             if child_sum == target:
#                 output.append(child.extract_vals())
#             print(child_sum)
#     return output
    
# root = TreeNode(5,
#         TreeNode(4,
#             TreeNode(11,
#                 TreeNode(7),
#                 TreeNode(2)
#             )
#         ),
#         TreeNode(8,
#             TreeNode(13),
#             TreeNode(4, None, TreeNode(1))
#         )
#     )

# target = 22
# print(tree_path_sum(root, target))

# def fib_matrix(n:int) -> int:
#     # Define matrix for fibonacci numbers
#     M = [
#         [1, 1],
#         [1, 0]
#     ]
#     sq = [
#         [1 * 1 + 1 * 1, 1 * 1 + 1 * 0], # [2, 1]
#         [1 * 1 + 0 * 1, 1 * 1 + 0 * 0], # [1, 1]
#     ]
#     cb = [
#         [2 * 1 + 1 * 1, 1 * 2 + 1 * 0], # [3, 2]
#         [1 * 1 + 1 * 1, 1 * 1 + 1 * 0], # [2, 1]
#     ]
#     frt = [
#         [3 * 1 + 2 * 1, 3 * 1 + 3 * 0], # [5, 3]
#         [2 * 1 + 1 * 1, 2 * 1 + 1 * 0], # [3, 2]
#     ]

# def fib_binary_search(n:int) -> int:
#     def helper(x): # 8
#         if x == 0:
#             return (0, 1)
#         a, b = helper(x // 2) # helper(4)
#         c = a * (2 * b - a) # 
#         d = a * a + b * b
#         if x % 2 == 0:
#             return (c, d)
#         else:
#             return (d, c + d)
        
        
        
    """
    n = 5; val = 5
    F[2n] = F[n] * (2F[n - 1] + F[n])
    F[10] = F[5] * (2F[4] + F[5])
    F[10] = 5 * (6 + 5) : 55
    0 1 1 2 3 5 8 13 21 34 55
    """
    
  