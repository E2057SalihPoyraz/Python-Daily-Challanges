# QUESTION:
# This is an interview question asked by Microsoft.
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
# Return its length: 4.

# 1:
def longest(nums):
    nums.sort()
    d = dict()
    for i in nums:
        d[i] = i
        if i-1 in d.keys():
            d[i] = d[i-1]           
    return (lambda y: y[0]-y[1]+1)(max(d.items(), key = lambda x: x[0]-x[1]))

# 2:
def longest2(nums):
    mx = 0
    adj = dict()
    for i in nums:
        if i in adj:
            continue
        lst = [i]*3
        if i - 1 in adj:
            lst[0] = adj[i - 1][0]
        if i + 1 in adj:
            lst[2] = adj[i + 1][1]
        for j in lst:
            adj[j] = lst[0], lst[2]
        mx = max(lst[2] - lst[0] + 1, mx)
    return mx