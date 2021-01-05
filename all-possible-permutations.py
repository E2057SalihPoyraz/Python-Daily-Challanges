# Problem :
# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input:
# [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

#1 :
lst, p = [1, 2, 3, 4], [[]]
for _ in lst:
    p = [[a] + b for a in lst for b in p if a not in b]
print(p)

#2:
a =  [1,2,3]
fin = [[x,y,z] for x in a for y in a for z in a if ( x != y and y != z and x != z )]
print(fin)

#3 :
lst, a = [1,2,3], []
for first in lst:
    for second in lst: 
        if second != first: 
            for third in lst: 
                if third != first and third != second: 
                    a.append([first , second , third])
print(a)    

#4 :
lst = [1,2,3]
r = [[]]
for _ in lst:
    r = [i + [j] for i in r for j in lst if j not in i]
print(r)

#5 :
nums = [1,2,3]
result_perms = [[]]
for n in nums:
    new_perms = []
    for perm in result_perms:
          for i in range(len(perm)+1):
            new_perms.append(perm[:i] + [n] + perm[i:])
            result_perms = new_perms
print(sorted(result_perms)) 