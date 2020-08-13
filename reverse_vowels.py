"""
Write a function that takes a string as input and reverse only the vowels of a string.

"""
VOWELS = set('aeiou')

def reverse_vowels(input_string):
    string = list(input_string)
    vowels = []
    indexes = []

    # loop through string to find vowels
    for x, y in enumerate(string):
        if y in VOWELS:
            vowels.append(y)
            indexes.append(x)

    # loop through tuple and replace characters
    for i, j in zip(indexes, reversed(vowels)):
        string[i] = j

    return ''.join(string)

print(reverse_vowels('hello')) # holle
print(reverse_vowels('lEetcode')) # leotcedE
print(reverse_vowels('anAconda')) # anocAnda