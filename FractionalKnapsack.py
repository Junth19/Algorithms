# Author : Junth Basnet
# Fractional Knapsack Problem
# Solution Strategy : Greedy Technique
# Time Complexity : O(nlogn)

"""
Input: number of weights (n), Weights w1, . . . , wn and values v1, . . . , vn of n items; capacity W .
Output: The maximum total value of fractions of items that fit into a bag of capacity W .

Sample:
Input:
4
10 40 20 30
60 40 100 120
50

Output:
Fraction Weight List : [10, 20, 20, 0]
Fraction Value List : [60, 100, 80, 0]
The maximum total value of fractions of items that fit into a bag : 240

"""

def FractionalKnapsack(n, weight, value, capacity):
    fraction_weight = [0] * len(value)
    fraction_value = [0] * len(value)
    total_value = 0

    for i in range(len(value)):
        if weight[i] <= capacity:
            fraction_weight[i] = weight[i]
            fraction_value[i] = value[i]
            total_value += value[i]
            capacity -= weight[i]
        else:
            fraction_weight[i] = capacity
            fraction_value[i] = int(capacity * value[i] / weight[i])
            total_value += (capacity * value[i]) / weight[i]
            break

    print("Fraction Weight List : {}".format(fraction_weight))
    print("Fraction Value List : {}".format(fraction_value))
    print("The maximum total value of fractions of items that fit into a bag : {}".format(int(total_value)))



n = int(input())
weight = [int(i) for i in input().split()]
value = [int(i) for i in input().split()]
capacity = int(input())

weight_value = list(sorted(zip(weight, value), key = lambda x:x[1] / x[0], reverse = True))
weight, value = [i[0] for i in weight_value], [i[1] for i in weight_value]

#print(weight)
#print(value)

FractionalKnapsack(n, weight, value, capacity)

