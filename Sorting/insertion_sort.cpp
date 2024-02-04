#include<iostream>
using namespace std;

void insertion_sort(int len, int arr[])
{
    int j;
    for (int i=1; i<len; i++)
    {
        j = i;
        while(arr[j-1] > arr[i] && j>0)
        {
            int temp = 0;
            temp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = temp;

            j -= 1;
        }
    }
}

int main()
{
    int len = 7, arr[] = {84, 5, 23, 52, 77, 91, 333};
    insertion_sort(len, arr);
    for(int i = 0; i<len; i++)
    {
        cout<<arr[i]<< ", ";
    }
    return 0;
}