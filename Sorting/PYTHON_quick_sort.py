def quicksort(arr, left, right):
    if left < right :
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)
        
def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i
            
            
my_list = [84, 5, 23, 52, 77, 91, 333]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)