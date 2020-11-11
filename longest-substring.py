# QUESTION: Interview Level = Medium
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
# Input: s = ""
# Output: 0

# 1:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = res = ""
        for i in s:
            if i not in temp:
                temp+=i
                if len(temp) > len(res):
                    res = temp
            else :
                temp = temp[temp.index(i)+1:] + i
        return len(res)

# 2:
def lengthOfLongestSubstring(s):
    smax, temp = "", ""
    for i in s:
        if i in temp:
            if len(temp) > len(smax):
                smax = temp
            while i in temp:
                temp = temp[1:]
        temp += i
    return max(len(smax),len(temp))

# 3:
def lengthOfLongestSubstring(s):
    smax, temp = 0, ""
    for i in s:
        if i in temp:
            smax = max(smax, len(temp))
            while i in temp:
                temp = temp[1:]
        temp += i
    return max(smax,len(temp))