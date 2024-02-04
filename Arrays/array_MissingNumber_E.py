#Find the missing number in the given array

# import array as ar

# # given_array = input(ar.array)
# # elements = given_array.split()


# max_arr = max(elements)

# for i in range(1, max_arr):
#     if i in elements:
#         pass
#     else:
#         print("The missing number is", i)

missingNumber= 0
N = int(input("Limit : "))
A = input("Arrays : ")
Array = A.split()

for i in range (1, N):
    if i in Array:
        continue
    else:
        missingNumber = i
        

print("The missing number is : ", missingNumber)

import array

# Step 1: Import the array module

# Step 2: Specify the type of elements (integer array)
arr_type = 'i'

# Step 3: Prompt the user for input
input_str = input("Enter the elements of the array, separated by spaces: ")

# Step 4: Convert the input and store it in the array
elements = input_str.split()
arr = array.array(arr_type, [int(elem) for elem in elements])

# Example usage: Print the array
print("Array:", arr)
