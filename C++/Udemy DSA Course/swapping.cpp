#include<iostream>

using namespace std;

void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;

    // cout<<&x<<endl;
    // cout<<&y<<endl;
}

int main()
{
    int a, b;
    a = 10;
    b = 20;

    // cout<<&a<<endl;
    // cout<<&b<<endl;

    swap(&a,&b);

    cout<<a<<" "<<b;
    return 0;
}