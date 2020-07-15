"""
Fast binary search challenge, find value in a sequence of numbers
"""

def binsearch(seq, value):

    l, h = 0, len(seq) - 1

    while l <= h:
        m = int((l + h) * 0.5)

        if seq[m] < value:
            l = m + 1
        elif value < seq[m]:
            h = m - 1
        else:
            return m
    return None

print(binsearch([0,0,0,1,5,8,10], 5)) # 4
print(binsearch([2,0,3,3,5,8,10,0], 8)) # 5

