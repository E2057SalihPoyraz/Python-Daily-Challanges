# QUESTION:
# This is an interview question asked by Yelp.
# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible
# letters the number could represent. You can assume each valid number in the mapping is a single digit.
# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return
# [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

# solution-1:

def f_mapping1(digits, mapping):
    return mapping[digits[0]] if len(digits) == 1 else [i+j for i in mapping[digits[0]] for j in f_mapping1(digits[1:], mapping)]

# solution-2:

def f_mapping2(digits, mapping):
    if len(digits) == 1:
        return mapping[digits[0]]
    result = []
    for i in mapping[digits[0]]:
        for j in f_mapping2(digits[1:], mapping):
            result.append(i + j)
    return result

# solution-3:

def f(dic,num):
    res=[""]
    for n in num:
        res=[i+j for i in res for j in dic[n]]
    return res
==============================
dic = {   "1":["a","b","c"],    "2":["d","e","f"],    "3": "g","h","i"]     }
num="123"
print(f(dic,num))