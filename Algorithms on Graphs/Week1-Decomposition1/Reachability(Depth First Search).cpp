// Author : Junth Basnet

//Reachability using Depth First Search
//Time Complexity : O(m + n)

/*
Input : Graph G and Source Vertex V
Output : The collection of vertices V of G so that there is a path from Source(S) to V
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
	int source;
	cin >> source;
	DepthFirstSearch(source);

	return 0;
}