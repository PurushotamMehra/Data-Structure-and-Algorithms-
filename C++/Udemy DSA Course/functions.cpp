#include<iostream>
using namespace std;


int add(int a, int b)
{
    int c;
    c = a +b;
    return c;
}
int main()
{
    int x = 10, y = 20, sum;
    sum = add(x,y);
    cout<<sum;
    return 0;
}
