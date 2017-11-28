//Greatest Common Factor Using Euclids Algorithm O(log min(a,b)
//Author@Junth Basnet
#include <iostream>
using namespace std;

int gcd(int a,int b)
{
	if(b==0)
	{
		return a;
	}
	else
	{
		return gcd(b,a%b);
	}
}

int main() 
{
	int a,b;
	cin>>a >>b;
	cout <<gcd(a,b);
	return 0;
}