# QUESTION:
# This is an interview question asked by Microsoft.
# Given an array of numbers, find the length of the longest increasing subsequence in the array.
# The subsequence does not necessarily have to be contiguous. For example, given the array
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has
# length 6: it is 0, 2, 6, 9, 11, 15.

def find_longest_sub2(lst):
    stack = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                stack[i] = max(stack[i], stack[j] + 1)
    return max(stack)

# Or;

data = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
from itertools import combinations
res=[]
for i in range(len(data),0,-1):
    c = list(combinations(data,i))
    for i in c:
        if list(i)==sorted(i):
            res=list(i)
            print(list(i))
            # break
    if res:
        break