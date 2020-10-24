# QUESTION:
# This is an interview question asked by Facebook.
# Given a list of integers, return the largest product that can be made by multiplying any three
# integers. For example, if the list is [-10, -10, 5, 2], we should return 500, since
# that's -10 * -10 * 5. You can assume the list has at least three integers.

def max_product(lst):
    lst.sort(reverse = True)
    return max(lst[0]*lst[1]*lst[2], lst[0]*lst[-1]*lst[-2])

# Or;

from math import inf
def max_product2(lst):
    maxn = [-inf, -inf, -inf, -inf]
    minn = [inf, inf, inf]
    for i in lst:
        for j in range(3):
            if i > maxn[j]:
                for k in range(j+1,3):
                    maxn[k] = maxn[k-1]
                maxn[j] = i
                break
        for j in range(2):
            if i < minn[j]:
                for k in range(j+1,2):
                    minn[k] = minn[k-1]
                minn[j] = i
                break
    return max(maxn[0]*maxn[1]*maxn[2], maxn[0]*minn[0]*minn[1])