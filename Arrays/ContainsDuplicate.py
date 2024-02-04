nums = [1,2,3,4]
ret_conf = False
flag_bool = False
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            flag_bool = True 
            break

if flag_bool == True:
    ret_conf = True
else :
    ret_conf= False

print(ret_conf) 