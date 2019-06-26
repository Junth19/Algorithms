# Author : Junth Basnet
# Collecting Signatures
# Solution Strategy : Greedy Technique
# Time Complexity : O(nlogn)

"""
Sample 1:
Input:
3
2 5
1 3
3 6

Output: 
1
3

Sample 2:
Input:
4
4 7
1 3
2 5
5 6

Output:
2
3 6
"""

n = int(input())
listOfCoordinates = [];
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    listOfCoordinates.append((a,b))

listOfCoordinates.sort(key = lambda x : x[1])

coOrdinates = []
index = 0

while index < n:
    currentCoordinate = listOfCoordinates[index]

    while index < n - 1 and currentCoordinate[1] >= listOfCoordinates[index + 1][0]:
        index += 1

    coOrdinates.append(currentCoordinate[1])
    index += 1
print(len(coOrdinates))
print(' '.join([str(i) for i in coOrdinates]))

