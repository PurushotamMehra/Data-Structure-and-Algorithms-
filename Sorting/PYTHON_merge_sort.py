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
merge_sort(my_list)
print(my_list)
    
        