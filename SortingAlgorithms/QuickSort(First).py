#Author : Junth Basnet
#Time Complexity varies from O(nlogn) to O(n^2)
#Solution Strategy : Divide and Conquer

"""
Sample 1:
Input:
2 10 5 3 8 7 4
Output:
2 3 4 5 7 8 10
"""


def quickSort(array, low, high):
    if low >= high:
        return array

    index = partition(array, low, high)
    quickSort(array, low, index - 1)
    quickSort(array, index + 1, high)
    return array


def partition(array, low, high):

    #First Element is considered to be pivot element
    pivot = array[low]
    j = low

    for i in range(low + 1, high + 1):
        if array[i] <= pivot:
            j = j + 1
            array[i], array[j] = array[j], array[i]

    array[j], array[low] = array[low], array[j]
    return j

array = [int(i) for i in input().split()]
sortedArray = quickSort(array, 0, len(array) - 1)
print(' '.join([str(i) for i in sortedArray]))