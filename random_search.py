"""
What's the worst way to search a sequence? Good as performance comparison with proper algorithms
"""
import random

def randomsearch(seq, value):
    while True:
        random_element = random.randint(0, len(seq)-1)
        if seq[random_element] == value:
            return random_element

print(randomsearch([0,0,0,1,5,8,10], 5)) # 4
print(randomsearch([2,0,3,3,5,8,10,0], 8)) # 5
