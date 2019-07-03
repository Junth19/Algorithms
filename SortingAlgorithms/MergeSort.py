# Author: Junth Basnet
# Implementation of merge sort
# Time Complexity: O(nlogn)
# Solution Strategy: Divide and Conquer

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftHalfArray = array[:mid]
        rightHalfArray = array[mid:]

        merge_sort(leftHalfArray)
        merge_sort(rightHalfArray)

        i = j = k = 0
        while i < len(leftHalfArray) and j < len(rightHalfArray):
            if leftHalfArray[i] < rightHalfArray[j]:
                array[k] = leftHalfArray[i]
                i = i + 1
            else:
                array[k] = rightHalfArray[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalfArray):
            array[k] = leftHalfArray[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalfArray):
            array[k] = rightHalfArray[j]
            j = j + 1
            k = k + 1
    return array

array = [int(i) for i in input().split()]
sort_array = merge_sort(array)
print(' '.join([str(i) for i in sort_array]))