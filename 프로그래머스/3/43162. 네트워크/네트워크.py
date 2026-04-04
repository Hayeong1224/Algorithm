def solution(n, computers):
    def dfs(cur):
        visited[cur] = True
        for nxt in range(n):
            if computers[cur][nxt] == 1 and not visited[nxt]:
                dfs(nxt)
        
    
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    return cnt