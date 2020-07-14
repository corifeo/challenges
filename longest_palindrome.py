"""
Another tricky challenge, probably not the most performant solution
because it's dirty brute force of all possible combinations and
regardless of the list comprehension is still very slow with long
strings
"""

from itertools import combinations

string = 'levelness radar poop'

def ispalindrome(s):
    return s == s[::-1] 

z = max([''.join(x) for i in range(len(string.replace(" ", ""))) for x in combinations(string.replace(" ", ""), i + 2) if ispalindrome(x)], key=len)

print(z)
