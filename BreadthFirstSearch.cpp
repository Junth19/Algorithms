//Author : Junth Basnet
//Implementation of Breadth First Search
//Time Complexity : O(m + n)


/*
n : number of nodes
m : number of edges
s : Source Vertex(node) from where the traversal begins

Input : n,m and edges(a,b)
Output : The order in which the nodes are visited(explored)
*/

#include<bits/stdc++.h>
#define pb push_back

using namespace std;

vector<bool>visited;
vector<vector<int> > adj;

void formEdge(int a, int b)
{
	//Directed Graph
	adj[a].pb(b);
	//For Undirected Graph
	//adj[b].pb[a];
}

void BreadthFirstSearch(int s)
{
	queue<int> q;
	q.push(s);
	visited[s] = true;

	while (!q.empty())
	{
		int f = q.front();
		q.pop();

		cout << f << " ";

		for (auto i = adj[f].begin(); i != adj[f].end(); i++)
		{
			if (!visited[*i])
			{
				q.push(*i);
				visited[*i] = true;
			}
		}
	}
}

int main()
{

	int n, m;
	std::cin >> n >> m;

	visited.assign(n, false);
	adj.assign(n, vector<int>());

	int x, y;
	for (int i = 0; i < m; i++) {
		std::cin >> x >> y;
		formEdge(x, y);
	}
	for (int i = 0; i < n; i++)
	{
		if (!visited[i])
		{
			BreadthFirstSearch(i);
		}
	}
	return 0;
}
