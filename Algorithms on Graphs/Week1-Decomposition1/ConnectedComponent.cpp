//Author : Junth Basnet
//Connected Components using Breadth First Search
//Time Complexity : O(m + n)

/*
Input : Graph G
Output : The connected components of G
Connected Component: The vertices of a graph G can be partitioned into Connected Components so that v 
is reachable from w if and only if they are in the same connected component
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

void ConnectedComponents(int s)
{
	queue<int> q;
	q.push(s);
	visited[s] = true;

	while (!q.empty())
	{
		int f = q.front();
		q.pop();

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
	int cc = 0;
	for (int i = 0; i < n; i++)
	{
		if (!visited[i])
		{
			cc += 1;
			ConnectedComponents(i);
		}
	}
	cout << cc;
	return 0;

}