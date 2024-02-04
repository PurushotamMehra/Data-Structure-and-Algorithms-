# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


def isAnagram(s, t):
    freq_s = {}
    for i in s:
        if i in freq_s:
            freq_s[i] += 1
        else:
            freq_s[i] = 1
            
    freq_t = {}
    for i in t:
        if i in freq_t:
            freq_t[i] += 1
        else:
            freq_t[i] = 1
            
    return freq_s == freq_t

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))
    