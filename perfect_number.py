# QUESTION:
# This is an interview question asked by Microsoft.
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.

def find_perfect_num2(n):
    number, count = 10, 0
    while count < n:
        number += 9
        if sum([int(i) for i in str(number)]) == 10:
            count += 1
    return number

# Second Solution;

def sum10(n):
    perf=[]
    x=0
    while len(perf)<n:
        if sum([int(a) for a in str(x)])==10: perf.append(x)
        x+=1       
    return perf[n-1]

# Third Solution;

num = 1
while True:
    num = input('pls enter a "positive" int number: ')
    if int(num) > 0:
        sum = 0
        for i in num:
            sum = sum+int(i)
        if sum % 10 == 0:
            a = int(num)//10
            print(f'\nsum of "{num}"s digits = "{sum}"')
        else:
            print(f'\nsum of "{num}"s digits = "{sum}" \nneed to add "{str(10 - sum % 10 )}" to end and now',"new number is", num + str(10 - sum % 10 ))
        break
    else:
        continue
