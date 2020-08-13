"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
VOWELS = [x for x in 'aeiou']

def reverse_vowels(input_string):
    # get a list of tuples for each vowel with position and character
    v_list = [(x, input_string[x]) for x in range(len(input_string)) if input_string[x].lower() in VOWELS]
    # split tuples in two indexes and letters, reverse indexes and rezip them in a dict
    r_list = dict(zip(list(zip(*v_list))[0][::-1], list(zip(*v_list))[1]))
    # loop through input_string and replace letters based on dict
    return ''.join([input_string[x] if x not in r_list else r_list[x] for x in range(len(input_string))])

print(reverse_vowels('hello')) # holle
print(reverse_vowels('lEetcode')) # leotcedE
print(reverse_vowels('anAconda')) # anocAnda