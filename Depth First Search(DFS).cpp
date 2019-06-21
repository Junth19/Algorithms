// Author : Junth Basnet
// Implementation of Depth First Search
// Time Complexity : O(m + n)

/*
Input: Graph G
Output: The order in which the nodes(vertices) are traversed
*/

/*
Example:
Input:
10 10
0 1
0 2
0 3
0 4
1 5
2 5
3 6
4 6
5 7
8 9
Output:
0 1 5 2 7 3 6 4 8 9
*/

#include<iostream>
#include<vector>

using namespace std;
vector<bool> visited;
vector <vector<int>> adj;

void formEdge(int a, int b)
{
	//Undirected Graph
	adj[a].push_back(b);
	adj[b].push_back(a);
}

void DepthFirstSearch(int s)
{
	cout << s << " ";
	visited[s] = true;
	for (auto i : adj[s])
	{
		if (!visited[i]) {
			DepthFirstSearch(i);
		}
	}
}

int main()
{

	int n, m;
	cin >> n >> m;
	visited.assign(n, false);
	adj.assign(n, vector<int>());
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		formEdge(a, b);
	}

	for (int i = 0; i < n; i++)
	{
		if (!visited[i])
		{
			DepthFirstSearch(i);
		}
	}
	
	return 0;
}
