def binary_search(arr, n):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left+(right - left) // 2
        
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9]
print(binary_search(arr,6))
            
     