def solution(n, wires):
    min_diff = n
    
    # 하나 끊고 양방향 간선 표시
    for i in range(n-1):
        graph = [[] for _ in range(n+1)]
        for j in range(n-1):
            if i == j:
                continue
                
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
            
        # dfs(스택으로 그룹 형성)
        visited = set()
        stack = [1]
        
        while stack:
            node = stack.pop()
            
            if node in visited:
                continue
        
            visited.add(node)
            
            # 다음 노드
            for nxt in graph[node]:
                if nxt not in visited:
                    stack.append(nxt)
        
        # 차이
        cnt = len(visited)
        min_diff = min(min_diff, abs((n - cnt) - cnt))
        
    return min_diff