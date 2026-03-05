from collections import deque
def split(w):
    open, close = 0, 0
    for i in range(len(w)):
        if w[i] == '(': 
            open += 1
        else: 
            close += 1
        if open == close:
            u = w[:i+1]
            v = w[i+1:] if i < len(w) - 1 else ''
            return u, v
    return u, v

def is_correct(w):
    q = deque()
    for b in w:
        if b == ')':
            if q: q.pop()
            else: return False
        elif b == '(': q.append('(')           
    
    if q: 
        return False
    return True

def check(w):
    if w == '': # 1
        return w
    
    u, v = split(w)

    if is_correct(u):
        return u + check(v)
    else:
        p = '(' + check(v) + ')'
        temp = ''
        for b in u[1:len(u) - 1]:
            temp += ')' if b == '(' else '('
        return p + temp
    
def solution(p):
    return check(p)