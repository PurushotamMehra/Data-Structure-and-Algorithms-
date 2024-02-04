#include<iostream>
#include<stdio.h>
using namespace std;

void FunB(int x);
void FunA(int x)
{
    if (x > 0)
    {
        cout<<x;
        FunB(x-1);    
    }
}

void FunB(int x)
{
    if(x>1)
    {
        cout<<x;
        FunA(x/2);
    }
}

int main()
{
    FunA(3);
    return 0;
}
