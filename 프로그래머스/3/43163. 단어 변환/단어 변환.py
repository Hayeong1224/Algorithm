from collections import deque

def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = set()
    visited.add(begin)
    
    while q:
        cur, dist = q.popleft()
        if cur == target:
            return dist
        
        for w in words:
            if w not in visited and w != cur:
                cnt = sum(1 if i != j else 0 for i, j in zip(w, cur))
                if cnt == 1:
                    visited.add(w)
                    q.append((w, dist+1))
        
    return 0