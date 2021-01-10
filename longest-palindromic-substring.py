# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, 
# find the longest palindromic substring in s.
# Example:
# Input: "banana"
# Output: "anana"
# Input: "million"
# Output: "illi"

#1 :
def long_palin(txt):
    a = []
    for i in range(len(txt)):
        for j in range(len(txt)-i):
            t=txt[i:(len(txt)-j)]
            if t == t[::-1]: 
                if not t in a:a.append(t)
    return(sorted(a, key=len, reverse = True)[0])        
long_palin("million") 

#2 :
x = "million"
a = ""
b = {}
for i in x:
    a += i
    if a in x[::-1]:
        b[a] = len(a)
    elif a != a[::-1]:
        a = a[1:]
max(b.keys(), key= lambda k: b[k])