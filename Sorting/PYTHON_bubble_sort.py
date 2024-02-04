def bubble_sort(arr):
    n = len(arr)
    
    #####################################################METHOD !#####################################################
    # for i in range(n):
    #     for j in range(0, n - 1 - i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]

    #####################################################METHOD 2#####################################################  
    # swap = False
    # while not swap:
    #     swap = True
    #     for i in range(1, n):
    #         if arr[i-1] > arr[i]:
    #             arr[i-1], arr[i] = arr[i], arr[i-1]
    #             swap = False
                
            
my_list = [84, 5, 23, 52, 77, 91, 333]
bubble_sort(my_list)
print(my_list)
                