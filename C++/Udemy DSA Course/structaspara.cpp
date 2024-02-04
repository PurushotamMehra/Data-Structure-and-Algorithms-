#include<iostream>
using namespace std;

class rectangle
{
    private:
        int length;
        int breadth;

    public:
        rectangle(int l, int b)
        {
            length = l;
            breadth = b;
            cout<<"Initialized Length : "<<length<<endl<<"Initialized breadth : "<<breadth<<endl;
        }

        void area()
        {
            int area = length * breadth;
            printf("Area : %d", area);
            cout<<endl;
        }

        void changelength(int len)
        {
            length = len;
            cout<<"Length : "<<length<<endl<<"Breadth : "<<breadth;
        }
};
int main()
{
    rectangle r(10,5);
    // r.initialize(20, 10);
    r.area();
    r.changelength(15);
    return 0;
}

