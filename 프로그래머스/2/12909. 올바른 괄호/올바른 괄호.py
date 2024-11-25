def solution(s):
    stack = []    
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop()
            if (i == '(' and x != ')') or (i == '{' and x != '}') or (i == '[' and x != ']'):
                return False
    if len(stack) != 0:
        return False
    return True