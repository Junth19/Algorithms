// Author : Junth Basnet
// Connected Components using Depth First Search
// Time Complexity : O(m + n)

/*
Defination:
The vertices of a graph G can be partitioned into Connected Components so that v is
reachable from w if and only if they are in the same connected component.

Input: Graph G
Output: The connected components of G

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
Connected Components: 2
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

	cout << "Connected Components: " << cc;


	return 0;
}