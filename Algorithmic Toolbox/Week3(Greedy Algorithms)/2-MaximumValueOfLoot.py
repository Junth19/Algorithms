#Author : Junth Basnet
#Maximum Value of Loot(Fractional Knapsack Problem)
#Solution Strategy : Greedy Technique
#Time Complexity : O(nlogn)

"""
Problem Description:
Input:
The frst line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines defne the values and weights of the items. The i-th line contains integers Vi and Wi—the
value and the weight of i-th item, respectively.

Output: 
The maximum value of fractions of items that ft into the knapsack.

Sample 1:
Input:
3 50
60 20
100 50
120 30

Output:
180.0

Sample 2:
Input:
1 10
500 30

Output:
166.66666666666669

"""

n, capacity = [int(i) for i in input().split()]
value = []
weight = []
for _ in range(n):
    v, w = [int(i) for i in input().split()]
    value.append(v)
    weight.append(w)
weight_value = list(sorted(zip(weight, value), key = lambda x : x[1] / x[0], reverse = True))
weight = [i[0] for i in weight_value]
value = [i[1] for i in weight_value]

max_value = 0
for i in range(n):
    if capacity == 0:
        print(max_value)
        #sys.exit() or quit() : both terminates the program
        quit()
    amount = min(capacity, weight[i])
    max_value += amount * (value[i] / weight[i])
    capacity -= amount
print(max_value)










