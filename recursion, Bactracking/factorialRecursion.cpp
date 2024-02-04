#include<iostream>
#include<stdio.h>
using namespace std;

int fact(int x)
{
    if (x == 0)
    {
        return 1;
    }
    return fact(x-1)*x;
}

int main()
{
    int c = fact(5);
    cout<<c;
    return 0;
}