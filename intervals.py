# QUESTION:
# This is an interview question asked by Snapchat.
# Given a list of possibly overlapping intervals, return a new list of intervals where all
# overlapping intervals have been merged. The input list is not necessarily ordered in any way.
# For example, given [(1, 3), (5, 8 ), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
# [[6, 8], [1, 9], [2, 4], [4, 7]]   -------> [1,9]
# [[1,3],[2,6],[8,10],[15,18]]  ------------> [[1,6],[8,10],[15,18]]

def fix_overlap(lst):
    lst.sort(key = lambda x:x[0])
    result = [list(lst[0])]
    for i in lst[1:]:
        if i[0] > result[-1][1]:
            result.append(list(i))
        else:
            result[-1][1] = max(result[-1][1], i[1])
    return [tuple(i) for i in result]

# Another Solution;

def fix_overlap2(lst):
    lst.sort(key = lambda x:x[0])
    start, end = lst[0]
    result = []
    for i in lst[1:]:
        if i[0] > end:
            result.append((start,end))
            start, end = i
        else:
            end = max(end, i[1])
    result.append((start,end))
    return result