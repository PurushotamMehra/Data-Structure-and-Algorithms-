def bubble_sort(arr):
    
    # n = len(arr)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    
    n = len(arr)
    swapped = False
    
    while not swapped:
        swapped = True
        
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i-1]
                swapped = False
                
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
        
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j - 1]

def merge_sort(arr):
    if len(arr) > 1 :
        right_arr = arr[:len(arr)//2]
        left_arr = arr[len(arr)//2:]
        
        merge_sort(right_arr)
        merge_sort(left_arr)
        
        right_index = 0
        left_index = 0
        sorted_index = 0
        
        while right_index < len(right_arr) and left_index < len(left_arr):
            if right_arr[right_index] < left_arr[left_index]:
                arr[sorted_index] = right_arr[right_index]
                right_index += 1    
            else:
                arr[sorted_index] = left_arr[left_index]
                left_index += 1
            sorted_index += 1
            
        while right_index < len(right_arr):
            arr[sorted_index] = right_arr[right_index]
            right_index += 1
            sorted_index += 1
            
        while left_index < len(left_arr):
            arr[sorted_index] = left_arr[left_index]
            left_index += 1
            sorted_index += 1 




my_list = [84, 5, 23, 52, 77, 91, 333]
insertion_sort(my_list)
print(my_list)
    