"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Input Format: The first and the only argument contains N integers in an array A.
Output Format: Return an integer, representing the minimum candies to be given.
"""

def candy(r):
    if len(r) <= 1:
        return len(r)

    c = [1] * len(r)

    for i in range(1, len(r)):
        if r[i] > r[i - 1]:
            c[i] = c[i - 1] + 1

    for i in range(len(r) - 1, 0, -1):
        if r[i - 1] > r[i]:
            c[i - 1] = max(c[i - 1], c[i] + 1)

    return c

test_value1 = [1, 0, 2, 3, 5]
print(candy(test_value1))    # [2, 1, 2, 3, 4]

test_value2 = [1, 2, 2, 1, 4]
print(candy(test_value2))    # [1, 2, 2, 1, 2]