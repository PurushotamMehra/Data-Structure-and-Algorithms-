def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            
my_list = [84, 5, 23, 52, 77, 91, 333]
insertion_sort(my_list)
print(my_list)