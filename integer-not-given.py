# QUESTION:
# This is an interview question asked by Google.
# Given an integer n and a list of integers, write a function that randomly generates a number 
# from 0 to n-1 that isn't in that given integer list.

# 1: 
def rand_int(lst, n):
    a=int(np.random.choice(range(0,n), 1))
    return a if a not in lst else rand_int(lst, n)

# 2:
from random import choice
def r_int(n, l):
    return choice([i for i in range(n) if i not in l])

# 3:
import random
lst5 = [i for i in range(n) if i not in lst]
print(random.choice(lst5))