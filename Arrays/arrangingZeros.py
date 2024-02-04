def rearrangingZeros(nums):
    ZeroArr = []
    Non_Zero = []
    for i in range(len(nums)):
        if nums[i] == 0:
            ZeroArr.append(nums[i])
            # arr.pop(i)
        else:
            Non_Zero.append(nums[i])
            
    nums = Non_Zero.extend(ZeroArr)
    return Non_Zero + ZeroArr


arr = [0, 1, 0, 3, 12]
print(rearrangingZeros(arr))