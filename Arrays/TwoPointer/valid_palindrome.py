def Palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

print(Palindrome("A man, a plan, a canal: Panama"))