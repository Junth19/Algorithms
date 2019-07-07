# Author : Junth Basnet
# Implementation of Depth First Search(DFS)
# Time Complexity : O(|E| + |V|)


def DFS(G, S):
    explored = set()
    stack = [S]

    while stack:
        u = stack.pop()
        if u in explored:
            continue
        explored.add(u)

        for v in G[u]:
            if v not in explored:
                stack.append(v)
    return explored


G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

print(DFS(G, 'A'))