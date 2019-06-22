//Author : Junth Basnet
//Application of Depth First Search(Topological Sorting)

/*
Input:
6 6
5 2
4 0
4 1
5 0
2 3
3 1

Output:
Vertex        Topological(Linear) Order
  0                      5
  1                      4
  3                      3
  2                      2
  4                      1
  5                      0
Topological(Linear Ordering) :
5 4 2 3 1 0
*/

#include<iostream>
#include<vector>
#include<stack>

using namespace std;
vector<bool> visited;
vector<vector<int> > adj;
stack<int> store;
int topologicalOrder = 5;

void formEdge(int a, int b)
{
	//Directed Graph
	adj[a].push_back(b);
}

void DepthFirstSearch(int s)
{
	visited[s] = true;
	for (auto i : adj[s])
	{
		if (!visited[i]) {
			DepthFirstSearch(i);
		}
	}
	cout << "  " << s << "                      " << topologicalOrder << endl;
	store.push(s);
	topologicalOrder -= 1;
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

	cout << "Vertex" << "        " << "Topological(Linear) Order" << endl;
	for (int i = 0; i < n; i++)
	{
		if (!visited[i])
		{
			DepthFirstSearch(i);
		}
	}
	cout << "Topological(Linear Ordering) : " << endl;
	while (!store.empty())
	{
		int top = store.top();
		cout << top << " ";
		store.pop();
	}
	return 0;
}