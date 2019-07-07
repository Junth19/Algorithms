# Author : Junth Basnet
# Implementation of Breadth First Search(BFS)
# Time Complexity : O(|E| + |V|)


def BFS(G, S):
    explored = set()
    queue = [S]

    explored.add(S)
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if v not in explored:
                queue.append(v)

                explored.add(v)
    return explored


G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}
print(BFS(G, 'A'))