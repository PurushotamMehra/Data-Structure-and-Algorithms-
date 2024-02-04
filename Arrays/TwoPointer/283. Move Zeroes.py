# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]


 
def moveZeroes(nums: list[int]) -> None:
#Method 1
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_count = nums.count(0)  
    non_zero_arr = [x for x in nums if x != 0]  
    zero_arr = [0] * zero_count 
    nums[:len(non_zero_arr)] = non_zero_arr
    nums[len(non_zero_arr):] = zero_arr

#Method 2
    # zero_count = nums.count(0)
    # non_zero_list = [num for num in nums if num != 0]
    # zero_arr = [0] * zero_count
    # nums[:] = non_zero_list + zero_arr
    print(nums)
    
    
nums = [0,1,0,3,12]
print(moveZeroes(nums))