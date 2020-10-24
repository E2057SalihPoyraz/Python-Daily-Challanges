# QUESTION:
# This is an interview question asked by ContextLogic.
# Implement division of two positive integers without using the division, multiplication, or 
# modulus operators. Return the quotient as an integer, ignoring the remainder.

# 1:
def div(m,n):
    result=0
    while n<=m:
        m-=n
        result+=1
    return result

# 2:
def div(x, y):  
    sign = -1 if ((x < 0) ^ (y < 0)) else 1    
    x, y = abs(x) , abs(y)    
    q = 0
    while (x >= y):  
        x -= y 
        q += 1      
    return sign * q

# 3:
def d(x, y, r=0, c=1): return r if x < y else d(x-y, y, r+c, c)