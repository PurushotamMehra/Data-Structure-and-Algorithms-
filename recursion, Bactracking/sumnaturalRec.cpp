#include<iostream>
#include<stdio.h>
using namespace std;

int Sum(int n)
{
    if (n == 0)
    {
        return 0;
    }
    return Sum(n-1) + n;
}

int main()
{
    int x = Sum(10);
    cout<<x;
    return 0;
}