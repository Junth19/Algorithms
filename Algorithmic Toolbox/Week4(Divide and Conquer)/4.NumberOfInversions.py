# Author: Junth Basnet
# Time Complexity: O(nlogn)
# Solution Strategy: Divide and Conquer

def merge(left, right):
    i = j = numberOfInversions = 0
    final = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
            numberOfInversions += 1
    final += left[i:]
    final += right[j:]

    return final, numberOfInversions


def merge_sort(array):
    global totalCOUNT
    if len(array) <= 1:
        return array


    mid = len(array) // 2
    leftHalfArray = array[:mid]
    rightHalfArray = array[mid:]

    # Two recursive calls on left and right half of array
    left = merge_sort(leftHalfArray)
    right = merge_sort(rightHalfArray)

    sorted_array, count  = merge(left, right)
    totalCOUNT += count

    return sorted_array


totalCOUNT = 0
n = int(input())
array = [int(i) for i in input().split()]
merge_sort(array)
print(totalCOUNT)