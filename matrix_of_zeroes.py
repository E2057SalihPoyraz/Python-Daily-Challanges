# QUESTION:
# This is an interview question asked by Facebook.
# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways
# of starting at the top-left corner and getting to the bottom-right corner. You can only move right
# or down. For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get
# to the bottom-right. Right, then down Down, then right Given a 5 by 5 matrix, there are 70 ways
# to get to the bottom-right.

def number_of_ways(N, M): 
    if(N == 1 or M == 1): 
        return 1
    return number_of_ways(N-1, M) + number_of_ways(N, M-1)

#Another solution:

import numpy as np

def num_ways(n, m):
    A = np.zeros((n,m-1), int)
    A[0] = np.ones(m-1)
    A = np.hstack([np.ones((n,1),  int), A])
    for i in range(1, n):
        for j in range(1, m):
            A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[-1][-1]