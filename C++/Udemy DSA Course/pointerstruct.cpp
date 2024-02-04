#include<iostream>
#include<stdio.h>
using namespace std;
struct rectangle
{
    int length;
    int breadth;
};

int main()
{
    // rectangle r = {10, 5};
    // cout<<r.length<<endl;
    // cout<<r.breadth<<endl;

    rectangle *p;
    // p = (struct rectangle *)malloc(sizeof(struct rectangle));
    p = new rectangle;

    p->length = 15;
    p->breadth = 7;

    // struct rectangle *p = &r;
    cout<<p->length<<endl;
    cout<<p->breadth<<endl;

    return 0;
}
