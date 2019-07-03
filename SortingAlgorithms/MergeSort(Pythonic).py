# Author: Junth Basnet
# Implementation of merge sort (Pythonic Way)
# Time Complexity: O(nlogn)
# Solution Strategy: Divide and Conquer

def merge(left, right):
    i = j = 0
    final = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    final += left[i:]
    final += right[j:]

    return final


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    leftHalfArray = array[:mid]
    rightHalfArray = array[mid:]

    # Two recursive calls on left and right half of array
    left = merge_sort(leftHalfArray)
    right = merge_sort(rightHalfArray)

    sorted_array = merge(left, right)
    return sorted_array

array = [int(i) for i in input().split()]
sort_array = merge_sort(array)
print(' '.join([str(i) for i in sort_array]))