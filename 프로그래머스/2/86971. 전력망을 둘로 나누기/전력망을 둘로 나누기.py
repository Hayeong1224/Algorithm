from collections import deque

def solution(n, wires):
    ans = n 
    
    for i in range(len(wires)): # 끊는 전선 선택
        
        adj = [[] for _ in range(n+1)]
        # i 제외 인접 리스트 만들기
        for idx, wire in enumerate(wires):
            if idx == i: continue
            adj[wire[0]].append(wire[1])
            adj[wire[1]].append(wire[0])
            
        # 네트워크 노드 세기
        visited = [False] * (n+1)
        q = deque([1])
        visited[1] = True
        cnt = 0
        
        while q:
            cur = q.popleft()
            cnt += 1
            
            for node in adj[cur]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True
        
        ans = min(ans, abs(cnt - (n - cnt)))
    
    return ans    