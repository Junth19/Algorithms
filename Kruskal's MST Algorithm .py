# Author : Junth Basnet
# Kruskal's Minimum Spanning Tree(MST) Algorithm
# Time Complexity : O(|E|log|V|)

"""
Sample(Geeks for Geeks):

Input:
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4

Output:

       EDGES
  NODE       NODE        COST
   2     -     3           4
   0     -     3           5
   0     -     1           10
Minimum Spanning Tree Cost: 19


"""

n, m = list(map(int, input().split()))
edges = []

for i in range(m):
    a, b, cost = list(map(int, input().split()))
    edges.append((i, a, b, cost))

edges = sorted(edges, key = lambda edge: edge[3])
parent = [i for i in range(n)]

def find_parent(i):
    if (i != parent[i]):
        parent[i] = find_parent(parent[i])
    return parent[i]


MSTCost = 0
MST = []

for edge in edges:
    parent_a = find_parent(edge[1])
    parent_b = find_parent(edge[2])

    if parent_a != parent_b:
        MSTCost += edge[3]
        MST.append(edge)
        parent[parent_a] = parent_b


print("       EDGES       ")
print("  NODE       NODE        COST")
for edge in MST:
    print("   {0}     -     {1}           {2}".format(edge[1], edge[2], edge[3]))

print("Minimum Spanning Tree Cost: {}".format(MSTCost))



