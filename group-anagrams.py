Group Anagrams
Given a list of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
============================================

#1:
def anagram(Input):
    a = {}
    for i in Input:
        x = "".join(sorted(i))
        if x in a:
            a[x].append(i)
        else:
            a[x] = [i]
    return list(a.values())
print(anagram(Input))

#2:
def anagram(lst):
    a,b,c=[], [], []
    for i in lst:
        if sorted(i) not in a:
            a.append(sorted(list(i)))
            b.append([])
    for j in range(len(b)):
        for k in lst:
            if sorted(k)==a[j]: b[j].append(k)
    for m in sorted(b, key=len, reverse=True):
        c.append(sorted(m))
    return c
anagram(["eat", "tea", "tan", "ate", "nat", "bat"])

#3:
def groupAnagrams(strs):
    anagrams = {}
    for i in strs:
        item = "".join(sorted(i))
        if item in anagrams:
            anagrams[item].append(i)
        else:
            anagrams[item]=[i]
    return anagrams.values()

#4:
A=["eat", "tea", "tan", "ate", "nat", "bat"]
C=[]
B=[]
for i in A:
    for j in A:
        if set(i)==set(j):
            C.append(j)
    if not C in B:
        B.append(C)
    C=[]
print(B)

#5 :
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anag = {}
for i in strs:
    if "".join(sorted(i)) in anag:
        anag["".join(sorted(i))].append(i)
    else:
        anag["".join(sorted(i))] = [i]
print(list(anag.values()))

#6 :
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = []
for j in strings:
    item = [x for x in strings if sorted(j) == sorted(x)]
    if item not in result:
        result.append(item)
print(result)