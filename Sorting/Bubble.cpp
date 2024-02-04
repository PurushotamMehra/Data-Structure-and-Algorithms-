#include<iostream>
using namespace std;

void Bubble_Sort(int len, int arr[])
{
    // for(int i = 0; i < len; i++){
    //     for(int j = 0; j < len-1-i; j++)
    //     {
    //         if (arr[j] > arr[j+1])
    //         {
    //             int temp = 0;

    //             temp = arr[j];
    //             arr[j] = arr[j+1];
    //             arr[j+1] = temp;
        
    //         }
    //     }
    // }

    bool swap = false;
    while(!swap)
    {
        swap = true;
        for(int i = 1; i < len; i++)
        {
            if(arr[i-1] > arr[i])
            {
                int temp = 0;
                temp = arr[i-1];
                arr[i-1] = arr[i];
                arr[i] = temp;
                swap = false;
            }
        }
    }

}

int main()
{
    int len = 7, arr[] = {84, 5, 23, 52, 77, 91, 333};
    Bubble_Sort(len, arr);
    for(int i = 0; i<len; i++)
    {
        cout<<arr[i]<< ", ";
    }
    return 0;
}