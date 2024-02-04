def findMin(nums):
    res = float("inf")
    
    l,r = 0, len(nums) - 1
    
    while l < r:
        mid = l+(r-l)//2
        res = min (res,nums[mid])
        
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1
    return min(res, nums[l])
nums = [3,4,5,1,2]
print(findMin(nums))