#Author : Junth Basnet
#Maximum Advertisement Revenue
#Solution Strategy : Greedy Algorithm
#Time Complexity : O(nlogn)-numbers to be sorted

"""
Problem Description:
Given two sequences a1, a2, ..., an (ai is the proft per click of the i-th ad) and b1, b2, ..., bn (bi is
the average number of clicks per day of the i-th slot), we need to partition them into n pairs (ai, bj)
such that the sum of their products is maximized.

Input Format:
The frst line contains an integer n, the second one contains a sequence of integers a1, a2, ..., an.
The third one contains a sequence of integers b1, b2, ..., bn.

Output Format:
The maximum advertisement revenue

Sample 1:
Input:
1
23
39

Output:
897

Sample 2:
Input:
3
1 3 -5
-2 4 1

Output:
23
"""


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a = sorted(a);
b = sorted(b); 

maxRevenue = sum([a[i] * b[i] for i in range(n)])
print(maxRevenue)





