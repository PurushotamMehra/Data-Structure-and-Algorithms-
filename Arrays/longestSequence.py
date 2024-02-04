
def longestConsecutive(nums: list[int]) -> int:
    hset = set(nums)
    maxCount = 0
    for num in hset:
        if num-1 not in hset:
            tmp = num
            while tmp in hset:
                maxCount = max(maxCount,tmp-num+1)
                tmp+=1
    return maxCount
        

print(longestConsecutive([100,4,200,1,3,2]))