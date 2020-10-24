# QUESTION:
# This is an interview question asked by Amazon.
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# For example, given the following matrix:
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

def movespiral(matrix):
    borders = [len(matrix[0]), len(matrix), -1, -1]
    opr = [1,1,-1,-1]
    pos = [0 , 0]
    dir = 0
    while True:
        print(matrix[pos[1]][pos[0]])
        i = dir % 2
        if pos[i] + opr[dir] == borders[dir]:
            return
        else:    
            pos[i] += opr[dir]
            if pos[i] + opr[dir] == borders[dir]:
                borders[dir-1] = pos[1-i]
                dir = (dir + 1) % 4   

# Another option:

import pandas as pd
N = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
df = pd.DataFrame(N)
a = list(df.loc[0])
df.drop(0, inplace=True)
b = list(df[4])
df.drop(4, axis=1, inplace=True)
c = list(df[df.columns[::-1]].loc[3])
df.drop(3, inplace=True)
d = list(df.iloc[::-1][0])
df.drop(0, axis=1, inplace=True)
e = list(df.loc[1])
df.drop(1, inplace=True)
f = list(df[df.columns[::-1]].loc[2])
whole = a + b + c + d + e + f
[print(i) for i in whole]