def twotarget(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        curr_target = nums[left] + nums[right]
        if curr_target == target:
            return [left, right]
        elif curr_target < target:
            left += 1
        else:
            right -= 1
            
    return None
             
nums = [2, 7, 11, 15]
target = 9
result = twotarget(nums, target)
print(result)