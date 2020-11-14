# QUESTION: Level of Interview Question = Easy
# Given a non-empty array of decimal digits representing a non-negative integer, increment one 
# to the integer. The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contains a single digit. You may assume the integer
# does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
# Input: digits = [9,9]
# Output: [1,0,0]
# Explanation: The array represents the integer 99.
# Example 3:
# Input: digits = [9]
# Output: [1,0]

# Çözüm-1
def plusOne2(digits):
    s = "".join([str(i) for i in digits])
    leftzeros = len(s) - len(str(int(s)))
    return [0]*leftzeros + [int(i) for i in str(int(s)+1)]

# Çözüm-2
def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        i=-1
        while -i <= len(digits) and (digits[i] == 9):
            digits[i] = 0
            i -= 1
        if i+1 == -len(digits):
            digits = [1] + digits
        else:
            digits[i] += 1
    return digits

    # çözüm 3:
    def addone(arr):
    num = int(''.join([str(i) for i in arr]))  # convert to int
    numback = num + 1 
    digits = [int(i) for i in str(numback)]  # convert to array
    return digits