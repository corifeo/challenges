"""
For an interview I had to come up with a piece of code that reads a number from STDIN
and tries to append the number 5 in all position to find the largest number, long story
short I rushed some code that didn't work and then later - after the interview - I've 
come up with this efficient solution.
"""

import sys

try: 
    output = max([int(str(sys.argv[1])[:x] + '5' + str(sys.argv[1])[x:]) 
                 for x in range(len(str(sys.argv[1]))) if str(sys.argv[1]).isdigit()])
    print(output)
except (ValueError, IndexError):
    sys.exit()