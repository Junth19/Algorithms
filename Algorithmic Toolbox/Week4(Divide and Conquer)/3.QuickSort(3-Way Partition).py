#Author : Junth Basnet
#Time Complexity : O(nlogn) [Randomized Quick Sort with nearly equal elements]
#Solution Strategy : Divide and Conquer

"""
Sample 1:
Input:
2 3 9 2 2
Output:
2 2 2 3 9
"""

from random import randint

def RandomizedQuickSort(array, low, high):
    if low >= high:
        return array

    #Generating random number and swapping it with the first element
    randomPivot = randint(low, high)
    array[low], array[randomPivot] = array[randomPivot], array[low]

    m1, m2 = partition3(array, low, high)
    RandomizedQuickSort(array, low, m1 - 1)
    RandomizedQuickSort(array, m2 + 1, high)
    return array


def partition3(array, low, high):

    #First Element is considered to be pivot element
    pivot = array[low]
    m2 = low

    for i in range(low + 1, high + 1):
        if array[i] <= pivot:
            m2 = m2 + 1
            array[i], array[m2] = array[m2], array[i]
    array[m2], array[low] = array[low], array[m2]

    m1 = low
    for i in range(low, m2):
        if array[i] < array[m2]:
            array[i], array[m1] = array[m1], array[i]
            m1 += 1
    return m1, m2





array = [int(i) for i in input().split()]
sortedArray = RandomizedQuickSort(array, 0, len(array) - 1)
print(' '.join([str(i) for i in sortedArray]))