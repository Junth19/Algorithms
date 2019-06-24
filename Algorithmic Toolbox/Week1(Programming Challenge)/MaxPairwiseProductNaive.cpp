// Author : Junth Basnet
// Programming Assignment: Programming Assignment 1: Maximum Pairwise Product(Naive Solution)

#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::max;

int MaxPairwiseProductNaive(const vector<int>& numbers)
{
	int product = 0;
	int n = numbers.size();
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			product = max(product, numbers[i] * numbers[j]);
		}
	}
	return product;
}

int main()
{
	int n;
	cin >> n;
	vector<int> numbers(n);
	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
	}

	int product = MaxPairwiseProductNaive(numbers);
	cout << product << "\n";
	return 0;
}