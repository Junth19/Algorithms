#Author : Junth Basnet
#Solution Strategy : Divide and Conquer
#Time Complexity : O(logn)

"""
Sample 1:
Input:
5 1 5 8 12 13
5 8 1 23 1 11

Output:
2 0 -1 0 -1

"""

def binarySearch(A, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            return binarySearch(A, mid + 1, high, key)
        else:
            return binarySearch(A, low, mid - 1, key)
    return -1

completeSEQ = [int(i) for i in input().split()]
searchSEQ = [int(i) for i in input().split()]
n = completeSEQ[0]
inputSEQ = completeSEQ[1:]


answerSEQ = []
for i in searchSEQ[1:]:
    result = binarySearch(inputSEQ, 0, n - 1, i)
    answerSEQ.append(result)

print(' '.join([str(i) for i in answerSEQ]))