#include<iostream>
using namespace std;

void selection_sort(int n, int arr[])
{
    for(int i = 0; i < n; i++)
    {
        int temp = 0;
        int min_index = i;
        for(int j = i+1; j<n; j++)
        {
            if(arr[min_index] > arr[j])
            {
                min_index = j;
            }
        }
        temp = arr[min_index];
        arr[min_index] = arr[i];
        arr[i] = temp;
    }
}

int main()
{
    int len = 7, arr[] = {84, 5, 23, 52, 77, 91, 333};
    selection_sort(len, arr);
    for(int i = 0; i<len; i++)
    {
        cout<<arr[i]<< ", ";
    }
    return 0;
}