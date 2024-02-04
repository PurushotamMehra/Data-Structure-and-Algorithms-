def validParenthesis(s):
    stack = []
    
    for i in s:
        if i in "({[":
            stack.append(i)
        else:
            if not stack :
                return False
            d = stack.pop()
            
            if (i == ')' and d != '(') or (i == ']' and d != '[') or (i == '}' and d != '{'):
                return False
    return not stack

s = "(]"
print(validParenthesis(s))