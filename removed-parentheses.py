# QUESTION:
# This is an interview question asked by Google.
# Given a string of parentheses, write a function to compute the minimum number of parentheses
# to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
# For example, given the string "()())()", you should return 1. Given the string ")(", you should
# return 2, since we must remove all of them.

# 1:
def f(text):
    while text != text.replace('()', ''):
        text=text.replace('()', '')
    return len(text)

# 2:
def parentheses(s):
    for i in range(len(s)):
        if "()" in s:
            s = s.replace("()","")
    return len(s)

# 3:
def checkform(text):
    total = [0,0]
    for i in text:
        if i == '(' :
            total[0] += 1
        elif i == ')' and total[0] > 0:
            total[0] -= 1
        else:
            total[1] += 1
    return sum(total)

# 4:
def checkform1(text):
    while '()' in text:
        text = text.replace('()', '')
    return len(text)

# 5:
# parantezin cinsi verilmediginden farkli tipteki parantezler icin
def num_parentheses(data):
    if data != data.replace('()', ''):
        data=data.replace('()', '')
    elif data != data.replace('{}', ''):    
        data=data.replace('{}', '')
    elif data != data.replace('[]', ''):    
        data=data.replace('[]', '')
    return len(data)