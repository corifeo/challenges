"""
You are given an unordered array consisting of consecutive integers without any duplicates. 
You are allowed to swap any two elements. You need to find the minimum number of swaps required
to sort the array in ascending order.

bubble sort is the best I can do in 10 minutes but problably there are shorter solutions

"""

def bubble_sort(nlist):
    swaps = 0
    for j in range(len(nlist)-1, 0, -1):
        for i in range(j):
            if nlist[i] > nlist[i+1]:
                # swap adjacent elements
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                swaps += 1
    return swaps

print(bubble_sort([4, 3, 1, 2])) 
print(bubble_sort([7, 1, 3, 2, 4, 5, 6]))
print(bubble_sort([2, 1, 3, 7, 4, 5, 6]))
print(bubble_sort([1, 3, 5, 2, 4, 6, 7]))
print(bubble_sort([7, 1, 3, 2, 4, 5, 6]))