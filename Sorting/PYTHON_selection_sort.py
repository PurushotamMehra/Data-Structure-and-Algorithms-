def selection_Sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j          
        arr[min_index], arr[i] = arr[i], arr[min_index]

                 
my_list = [84, 5, 23, 52, 77, 91, 333]
selection_Sort(my_list)
print(my_list)
                