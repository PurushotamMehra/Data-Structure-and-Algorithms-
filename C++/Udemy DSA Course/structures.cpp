#include<iostream>
using namespace std;

struct Rectangle
{
    int length;
    int breadth; 
};

int main()
{
    // struct Rectangle r;
    struct Rectangle r = {10, 5};
    cout<<"Area of rectangle : "<<r.length*r.breadth;

}
