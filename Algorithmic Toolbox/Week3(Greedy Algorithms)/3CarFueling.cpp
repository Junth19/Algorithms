//Author : Junth Basnet
//Car Fueling Problem (Greedy Algorithm)
//Time Complexity : O(n)

/*
Solution Strategy : Greedy Algorithm
To refill at the farthest reachable gas station is a safe move.

Input:
The frst line contains an integer d. The second line contains an integer m. The third line
specifes an integer n. Finally, the last line contains integers stop1, stop2, . . . , stopn.

Output :
Minimum number of reflls needed. Assuming that the car starts with a full tank. If it is not possible to
reach the destination, output −1.

Sample 1:
Input :
950
400
4
200 375 550 750

Output :
2

*/


#include <iostream>
#include <vector>
#include<cstdlib>

using namespace std;
using std::cin;
using std::cout;
using std::vector;

int compute_min_refills(int travel_distance, vector<int>& stops) {

	int currentRefill = 0;
	int numRefill = 0;
	int lastRefill = 0;
	int n = stops.size() - 2;
	int tempTravelDistance = travel_distance;


	while (currentRefill <= n)
	{
		lastRefill = currentRefill;
		travel_distance = tempTravelDistance;
		while (currentRefill <= n && stops[currentRefill + 1] - stops[currentRefill] <= travel_distance)
		{
			travel_distance = travel_distance - (stops[currentRefill + 1] - stops[currentRefill]);
			currentRefill = currentRefill + 1;
		}
		if (currentRefill == lastRefill)
		{
			return -1;
		}
		if (currentRefill <= n)
		{
			numRefill += 1;
		}
	}
	return numRefill;
}


int main() {
	int d = 0;
	cin >> d;
	int m = 0;
	cin >> m;
	int n = 0;
	cin >> n;

	vector<int> stops(n + 2);
	for (size_t i = 1; i <= n; ++i)
		cin >> stops.at(i);

	//Initial Position
	stops.at(0) = 0;
	//Final Position
	stops.at(n + 1) = d;

	int minRefillNumber = compute_min_refills(m, stops);
	cout << minRefillNumber;

	return 0;
}
