// Author : Junth Basnet
// Programming Assignment: Programming Assignment 1: Maximum Pairwise Product(Optimized Solution)

#include<iostream>
#include <vector>
#include<algorithm>

using std::cin;
using std::cout;
using std::max;

long long MaxPairwiseProductFast(std::vector<int>& numbers)
{
	int n = numbers.size() - 1;
	sort(begin(numbers), end(numbers));
	return (long long)numbers[n] * numbers[n - 1];
}

int main()
{
	int n;
	cin >> n;
	std::vector<int> numbers(n);
	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
	}

	int product = MaxPairwiseProductFast(numbers);
	cout << product << "\n";
	return 0;
}