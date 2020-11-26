# QUESTION: Level of Interview Question = Easy
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# Example 1:
# Input: 1; Output: "A"
# Example 2:
# Input: 28; Output: "AB"
# Example 3:
# Input: 701; Output: "ZY"


# çözüm-1:
def reply(input):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = list(range(1,27))
    data = dict(zip(num, letters))
    if input < 27 :
        return data[input]
    else:
        first = data[input // len(letters)]
        second = data[input % len(letters)]
        return first+second

# çözüm-2:
def convertToTitle(n):
    result = ""
    while n > 26:
        result = chr(65+(n-1)%26)  + result  
        n = (n-1) // 26
    return chr(64+n) + result  