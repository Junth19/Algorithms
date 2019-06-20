//Author : Junth Basnet
//Reachability using Breadth First Search
//Time Complexity : O(m + n)

/*
Input : Graph G and Source Vertex V
Output : The collection of vertices V of G so that there is a path from Source(S) to V
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

void Reachability(int s)
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

	int source;
	cin >> source;
	Reachability(source);
	return 0;

}