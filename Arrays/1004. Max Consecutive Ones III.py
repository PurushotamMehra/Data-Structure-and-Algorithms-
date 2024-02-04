# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

# def longestOnes(A: List[int], K: int) -> int:
#     i = 0
#     max_len = 0
#     for j in range(len(A)):
#         if A[j] == 0:
#             K -= 1
#         while K < 0:
#             if A[i] == 0:
#                 K += 1
#             i += 1
#         max_len = max(max_len, j - i + 1)
#     return max_len

def longestOnes(nums: list[int], k: int) -> int:
    i = 0
    max_len = 0
    
    for K in range(len(nums)):
        if nums[k] == 0:
            k -= 1
        while k < 0:
            if nums[i] == 0:
                k += 1
            i += 1
        max_len = max(max_len, k-i+1)
    return max_len
 
nums = [1,1,1,0,0,0,1,1,1,1,0]
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 2
print(longestOnes(nums, k))