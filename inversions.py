# QUESTION:
# This is an interview question asked by Google.
# We can determine how "out of order" an array A is by counting the number of inversions it has.
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element
# appears after a larger element. Given an array, count the number of inversions it has. Do this
# faster than O(N^2) time. # You may assume each element in the array is distinct.
# For example;
# A sorted list has zero inversions.
# The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
# The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

# 1:
def inv_num(lst):
    count=0
    lst2=lst.copy()
    for i in lst:
        lst2.remove(i)
        for j in lst2:
            if i>j:
                count+=1
    return count

# 2:
def f_inversion(nums):
    result = []
    for i in nums:
        result += [j + [i] for j in result]
        result.append([i])
    return len(list(filter(lambda x: x[0] > x[1], (filter(lambda x: len(x) == 2, result)))))

# 3:
def f_inversion1(nums):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
    return count

# 4:
def f_inversion2(nums):
    return len([1 for i in range(len(nums)-1) for j in range(i+1, len(nums)) if nums[i] > nums[j]])