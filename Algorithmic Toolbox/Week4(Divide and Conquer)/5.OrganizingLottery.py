# Author : Junth Basnet
# Time Complexity : O(n)

"""
Sample1:
Input:
2 3
0 5
7 10
1 6 11

Output:
1 0 0

Sample2:
Input:
1 3
-10 10
-100 100 0

Output:
0 0 1
"""

s, p = [int(i) for i in input().split()]
listInfo = []

for i in range(s):
    a, b = [int(i) for i in input().split()]
    listInfo.append((a, 'l'))
    listInfo.append((b, 'r'))

points = input().split()
for i in points:
    listInfo.append((int(i), 'p'))

listInfo.sort()
segmentCOUNT = 0
countDict = {}
for i in listInfo:
    if i[1] == 'l':
        segmentCOUNT += 1
    elif i[1] == 'r':
        segmentCOUNT -= 1
    else:
        countDict[i[0]] = segmentCOUNT

answerList = []
for i in points:
    answerList.append(countDict[int(i)])

print(' '.join([str(i) for i in answerList]))


