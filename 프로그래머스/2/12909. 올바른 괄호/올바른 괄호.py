def solution(s):
    stack = []
    for cur in s:
        if cur == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append('(')
                
    return True if len(stack) == 0 else False # stack 비어있으면 true