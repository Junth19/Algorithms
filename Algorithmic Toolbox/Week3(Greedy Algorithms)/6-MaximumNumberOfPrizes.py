# Author : Junth Basnet
# Maximum Number of Prizes
# Solution Strategy : Greedy Technique
# TIme Complexity : O(n)

"""
Sample 1.
Input:
6
Output:
3
1 2 3

Sample 2:
Input:
8
Output:
3
1 2 5

Sample 3.
Input:
2
Output:
12
"""

n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()

candiesDivided = []
remaining = n
for i in range(1, n):
    if remaining > 2 * i:
        candiesDivided.append(i)
        remaining -= i
    else:
        candiesDivided.append(remaining)
        break
print(len(candiesDivided))
print(' '.join([str(i) for i in candiesDivided]))









