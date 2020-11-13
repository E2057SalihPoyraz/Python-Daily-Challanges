# QUESTION: Level of Interview Question = Easy
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word (last word means the last appearing word if we loop from
# left to right) in the string. If the last word does not exist, return 0.
# Example:
# Input: "Hello World"
# Output: 5

def last_word(words:str) -> int:
    words_list = words.split()
    if len(words_list) < 2:
        return 0
    else:
        return len(words_list[-1])
print(last_word("World"))