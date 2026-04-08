from collections import deque

def solution(n, edge):
    # 간선 길이가 동일 -> BFS 해도 되겠다!
    # 인접 리스트부터 구하기!
    adj = [[] * (n+1) for _ in range(n+1)]
    visited = [False] * (n+1)
    for n1, n2 in edge:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    # BFS - 1번 노드 시작, (노드, dist) 넣어서 maxDist를 갱신하면 될 듯!
    maxDist = 0
    maxNodeCnt = 0  
    q = deque([(1,0)])
    visited[1] = True
    
    while q:
        cn, dist = q.popleft()

        if maxDist < dist:
            maxDist = dist
            maxNodeCnt = 1
        elif maxDist == dist:
            maxNodeCnt += 1
        
        for n in adj[cn]:
            if not visited[n]:
                q.append((n, dist + 1))
                visited[n] = True
        
    return maxNodeCnt