# Author : Junth Basnet
# Money Change
# Solution Strategy : Greedy Algorithm
# Time Complexity : O(1) 

"""
Task. The goal in this problem is to fnd the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer m.
Constraints. 1 ≤ m ≤ 10^3.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.

Sample 1:
Input:
2
Output:
2

Sample 2:
Input:
28
Output:
6
"""

m = int(input())
minCoins = 0
remainder = 0
if m >= 10:
    minCoins += (m // 10)
    remainder = (m % 10)
    m = remainder
if m >= 5:
    minCoins += (m // 5)
    remainder = (m % 5)
    m = remainder
if m >= 1:
    minCoins += m
print(minCoins)
   
