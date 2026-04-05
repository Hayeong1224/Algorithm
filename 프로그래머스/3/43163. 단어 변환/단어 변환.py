from collections import deque

def is_enable_to_change(a, b):
    return sum (1 for c1, c2 in zip(a,b) if c1 != c2) == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = set([begin])
    
    while q:
        cur, dist = q.popleft()
        
        if cur == target:
            return dist
        
        for w in words:
            if is_enable_to_change(cur,w):
                visited.add(w)
                q.append((w, dist + 1))
                
    return 0