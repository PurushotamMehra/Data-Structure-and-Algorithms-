#include<iostream>
using namespace std;

// void fun(int * A, int n)
// {
//     // cout<<sizeof(A)/sizeof(int)<<endl;
//     for (int a = 0; a<n; a++)
//     {
//         cout<<A[a]<<" ";
//     }

// }

// int main()
// {
//     int A[] = {2, 4, 6, 8, 7};
//     int n = 5;
//     fun(A, n);
//     cout<<endl;
//     // cout<<sizeof(A)/sizeof(int)<<endl;
//     for (int x : A)
//     {cout<<x<<" ";}
    
//     return 0;
// }
int * fun(int size)
{
    int *p;
    p = new int[size];

    for(int i = 0; i<size; i++)
    {
        p[i] = i+1;
    }

    return p;
}

int main()
{
    int *ptr, len;
    len = 5;

    ptr = fun(len);

    for(int j = 0; j < len; j++)
    {
        cout<<ptr[j]<<endl;
    }

    return 0;
}