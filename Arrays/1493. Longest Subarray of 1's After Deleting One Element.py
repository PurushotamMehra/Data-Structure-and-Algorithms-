# 1493. Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.


# def longestSubarray(nums: list[int]) -> int:
#     max_len = 0
#     zero_count = 1
#     i,j = 0, 0 
    
#     while j < len(nums):
#     # for j in range(len(nums)):
#         if nums[j] == 0:
#             zero_count -= 1
#         while zero_count <= 0:
#             if nums[i] == 0:
#                 zero_count += 1    
#             i += 1
        
#         max_len = max(max_len, j - i + 1)
#         j += 1
    
#     return max_len - 1 if max_len > 0 else 0

def longest_subarray(nums):
    max_len = 0
    left, right = 0, 0
    zero_count = 0

    while right < len(nums):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len - 1 if max_len > 0 else 0

# # Example usage:
# nums1 = [1, 1, 0, 1]
# print(longest_subarray(nums1))  # Output: 3

# nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
# print(longest_subarray(nums2))  # Output: 5

# nums3 = [1, 1, 1]
# print(longest_subarray(nums3))  # Output: 2

# # nums = [1,1,0,1]
# print(longest_subarray(nums))