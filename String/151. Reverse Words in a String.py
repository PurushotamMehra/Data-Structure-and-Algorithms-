# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

def reverseWords(s: str) -> str:
    # temp = ''
    # result_String = []

    # for i in s:
    #     if i == ' ' and temp :
    #         result_String.append(temp)
    #         temp = ''
    #     elif i != ' ':
    #         temp += i
    # if temp:
    #     result_String.append(temp)
    
    # return ' '.join(reversed(result_String))        

    # split_str = s.split(' ')
    # return ' '.join(reversed(split_str))

    return ' '.join(reversed(s.split()))


    
s = "  hello world  "

print(reverseWords(s))

            
            
            