//Author : Junth Basnet
//Iterative Selection Sort

#include<bits/stdc++.h>
#include <iterator>

using namespace std;

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int *selectionSort(int array[], int length)
{
	int minimum;
	for (int i = 0; i < length - 1; i++) {
		minimum = i;

		for (int j = i + 1; j < length; j++) {
			if (array[j] < array[minimum]) {
				minimum = j;
			}
		}
		swap(&array[i], &array[minimum]);
	}

	return array;

}

int main() {
	int array[] = { 1,3,4,2,5 };
	int *sortedArray = selectionSort(array, 5);
	int arrayLength = sizeof(array) / sizeof(*array);
	for (int i = 0; i < arrayLength; i++) {
		cout << sortedArray[i];
	}
	return 0;
}