"""
Same as the previous challenge but I was asked to use the least possible number of loops,
I would have prefered a neater list comprehension but breaking out a loop would have 
required additional libraries or funky exception raising functions.
"""
import sys

try: 
    string = list(sys.argv[1])
    for x in range(len(string)):
        if int(string[x]) < 5:
            print(string[:x] + ['5'] + string[x:])
            break
except (ValueError, IndexError):
    sys.exit()

