def groupAnagrams(str):
    sol = {}
    for i in str:
        count = [0] * 26
        for j in i:
            count[ord(j) - ord("a")] += 1
            
        key = tuple(count)
        if key in sol:
            sol[key].append(i)
        else:
            sol[key] = [i]
    return list(sol.values())
        
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))