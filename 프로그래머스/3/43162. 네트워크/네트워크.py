def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(x):
        visited[x] = 1
        for i in range(n):
                if computers[x][i] == 1 and not visited[i]:
                    dfs(i)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer