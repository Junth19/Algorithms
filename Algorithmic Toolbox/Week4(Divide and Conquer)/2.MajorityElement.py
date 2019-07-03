# Author : Junth Basnet
# Solution Strategy : Hashmap
# Time Complexity : O(n)
# Space Complexity : O(n)

"""
Sample 1:
Input:
5
2 3 9 2 2
Output:
1

Sample 2:
Input:
4
1 2 3 4
Output:
0

"""

def numberMajorityElement(A, n):
    dictCOUNT = {}
    for i in range(n):
        if A[i] not in dictCOUNT:
            dictCOUNT[A[i]] = 1
        else:
            dictCOUNT[A[i]] += 1

    countCHECK = 0
    for key in dictCOUNT:
        if dictCOUNT[key] > n / 2:
            countCHECK += 1
    print(countCHECK)



n = int(input())
inputSEQ = [int(i) for i in input().split()]
numberMajorityElement(inputSEQ, n)