def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    
    def dfs(cur_k, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and cur_k >= dungeons[i][0]:
                visited[i] = True
                dfs(cur_k - dungeons[i][1], cnt+1)
                visited[i] = False
    
    dfs(k, 0)
    return answer