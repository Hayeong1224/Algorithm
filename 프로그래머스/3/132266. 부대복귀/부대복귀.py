from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    # destination에서 모든 노드까지 거리 구하기    
    dist_map = [-1] * (n+1)
    q = deque([destination])
    dist_map[destination] = 0
    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if dist_map[next] == -1:
                q.append(next)
                dist_map[next] = dist_map[cur] + 1
    
    result = []
    for node in sources:
        result.append(dist_map[node])
        
    return result