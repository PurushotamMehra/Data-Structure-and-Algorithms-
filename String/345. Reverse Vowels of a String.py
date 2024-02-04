# 345. Reverse Vowels of a Sing
# Given a sing s, reverse only all the vowels in the sing and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

def reverseVowels(s):
    l, r = 0, len(s) - 1
    s_list = list(s)
    # vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    vowels = set('aAeEiIoOuU')
    while l < r:
        if s_list[l] in vowels and s_list[r] in vowels:
            s_list[l], s_list[r] = s_list[r], s_list[l]  # Swap the vowels
            l += 1
            r -= 1
        elif s_list[r] not in vowels:
            r -= 1
        elif s_list[l] not in vowels:
            l += 1
            
    return ''.join(s_list)

s = "aA"
print(reverseVowels(s))

# def reverseVowels(s):
#     l, r = 0, len(s) - 1
#     s_list = list(s)
#     vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])  # Include uppercase vowels
#     while l < r:
#         if s_list[l] in vowels and s_list[r] in vowels:
#             s_list[l], s_list[r] = s_list[r], s_list[l]  # Swap the vowels
#             l += 1
#             r -= 1
#         elif s_list[l] not in vowels:
#             l += 1
#         elif s_list[r] not in vowels:
#             r -= 1
            
#     return ''.join(s_list)

# s = "hello"
# print(reverseVowels(s))

    