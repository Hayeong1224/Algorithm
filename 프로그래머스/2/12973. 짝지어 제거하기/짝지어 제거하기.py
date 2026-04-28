def solution(s):
    stack = []
    for i, c in enumerate(s):
        if not stack:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    if not stack:
        return 1
    else:
        return 0