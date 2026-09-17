def solution(tickets):
    
    def dfs(cur, path):
        if len(path) == len(tickets) + 1:
            return path
        
        # 다음 목적지 찾아 가기
        for i, (depart, dest) in enumerate(tickets):
            if depart == cur and not visited[i]:
                visited[i] = True
                result = dfs(dest, path + [dest])
                
                if result: # 정답 찾았으면 전달
                    return result
                
                visited[i] = False
        return None
                
    # 목적지를 알파벳 순서대로 정렬
    tickets.sort(key=lambda x: x[1])
    visited = [False] * len(tickets)
    
    return dfs("ICN", ["ICN"])