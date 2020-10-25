# QUESTION:
# This is an interview question asked by Palantir.
# Given a number represented by a list of digits, find the next greater permutation of a number,
# in terms of lexicographic ordering. If there is not greater permutation possible, return the
# permutation with the lowest value/ordering.
# For example;
# the list [1,2,3] should return [1,3,2]
# the list [1,3,2] should return [2,1,3]
# the list [3,2,1] should return [1,2,3]
# NOTE: What is lexicographic permutation?
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
# of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are: 012 021 102 120
# 201 210.

#1:
def nexperm(lst):
    i = len(lst)-2
    while i >= 0 and lst[i] >= lst[i+1]:
        i -= 1
    if i >= 0:
        j = len(lst)-1
        while j>0 and lst[j] <= lst[i]:
            j -= 1
        lst[i], lst[j] = lst[j], lst[i]
    lst[i+1:len(lst)] = reversed(lst[i+1:len(lst)])
    return lst

# 2:
from itertools import permutations
def nexperm2(lst):
    perm = sorted(list(permutations(lst)))
    i = perm.index(tuple(lst))
    return perm[i+1] if i < len(perm)-2 else perm[0]