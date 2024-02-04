
def mergeAlternately(word1: str, word2: str):
    i,j = 0,0
    new_str = ''

    while i<len(word1) or j<len(word2):
        if i != len(word1):
            new_str += word1[i]
            i += 1
        if j != len(word2):
            new_str += word2[j]
            j += 1
    return new_str
    
print(mergeAlternately('abc', 'pqr'))
        
