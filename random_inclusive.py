# QUESTION:
# This is an interview question asked by Two Sigma.
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
# implement a function rand5() that returns an integer from 1 to 5 (inclusive).

# solution-1:

def rand5():
    x=rand7()
    while x<6:
        return x
    else:
        return rand5()

# solution-2:

def rand5():
    x = rand7()
    return x if 1 <= x <= 5 else rand5()

# solution-3:

def rand5():
    return int ((rand7()/7)*5)