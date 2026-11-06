from collections import deque
def solution(n, computers):
    visited = set()
    ans = 0
    
    for c in range(n):
        if c not in visited:
            ans += 1
            q = deque([c])
            
            while q:
                cur = q.popleft()
                visited.add(cur)
                
                for nxt in range(n):
                    if computers[cur][nxt] and nxt not in visited:
                        q.append(nxt)
                        
    return ans
            