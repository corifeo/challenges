"""
Given an array 'a' of 'n' integers and a number 'd' perform left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.

Probably one of the easiest challenges as of today
"""


def left_rotate(a, d):
  return a[-d % len(a):] + a[:-d % len(a)]


# Rotate by 1
print(*left_rotate([20, 10, 34, 34, 1, 5, 99], 1), sep=' ')
# Rotate by 2
print(*left_rotate([33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97], 2), sep=' ')
# Rotate by 3
print(*left_rotate([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 3), sep=' ')