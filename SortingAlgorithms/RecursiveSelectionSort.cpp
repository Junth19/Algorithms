//Author : Junth Basnet
//Recursive Selection Sort

#include<bits/stdc++.h>
using namespace std;

int * recursiveSelectionSort(int array[], int length, int startIndex = 0) {
	//Base case of recursion
	if (startIndex >= length - 1) {
		return array;
	}
	int minimum = startIndex;
	for (int j = startIndex + 1; j < length; j++) {
		if (array[j] < array[minimum]) {
			minimum = j;
		}
	}
	swap(array[minimum], array[startIndex]);
	//Recursive call
	recursiveSelectionSort(array, length, startIndex + 1);
	return array;
}

int main() {
	int array[] = { 1,5,3,2,4 };
	int length = sizeof(array) / sizeof(*array);
	int *sortedArray = recursiveSelectionSort(array, length);
	for (int i = 0; i < length; i++) {
		cout << sortedArray[i];
	}
	return 0;
}