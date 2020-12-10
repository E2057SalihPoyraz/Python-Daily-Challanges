# Python tip
# You can use the Counter class to check whether two strings are anagrams!

from collections import Counter

def is_anagram(str_1, str_2):
    """
    Returns whether the two strings provided are anagrams.
    Keyword arguments:
    str_1 -- The first string
    str_2 -- The second string
    """
    return Counter(str_1) == Counter(str_2)

print(is_anagram("RACECAR", "CARRACE"))
