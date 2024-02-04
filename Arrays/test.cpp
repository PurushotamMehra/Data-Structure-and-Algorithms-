// // #include<iostream>
// // #include<stdio.h>

// // using namespace std;

// // int main()
// // {
// //     int a = 2;
// //     int b = ++a + a++;
// //     cout << b << endl;
// // }

// int fun(Node *root)
// {
//     if(root == NULL)
//         return 0;

//     return fun(root -> left) + fun(root -> right)
// }

#include<iostream>
using namespace std;

int main()
{
    int x, y, z;
    z=4;
    x=5;
    y=9;

    while(--x)
    {
        x = z+1;
        y = x-z;
        z= y/2;
    }
    cout<<z;
    return 0;
}