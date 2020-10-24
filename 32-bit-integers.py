# QUESTION:
# This is an interview question asked by Facebook.
# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical
# or bit operations. You can assume b can only be 1 or 0.

# solution-1:

def funn(x,y,b):
    return x*b + y*(1-b)

# solution-2:

print(x*b + y*(1-b))

# solution-3:

def check(x,y,b):
    return x*b | y*(1-b)