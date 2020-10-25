# QUESTION:
# This is an interview question asked by Microsoft.
# Given a number in the form of a list of digits, return all possible permutations without using
# any permutation function/method of any library, such as itertools.permutations.
# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

# 1:

data = ["a", "b", "c", "d"]
res=[""]
for i in data:
    res=[j+k for j in res for k in data if k not in j]

# 2:

def perm(lst):    
    r = [[]]
    for _ in lst:
        r = [i + [j] for i in r for j in lst if j not in i]
    return r