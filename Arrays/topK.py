def topKFrequent(nums: list[int], k: int) :
    freq_dict = {}
    for i in nums:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
            
    return sorted(freq_dict, key = freq_dict.get, reverse=True)[:k]
    
        

# Example usage:
my_list = [1,1,1,2,2,3]
result_dict = topKFrequent(my_list, 2)

print(result_dict)
