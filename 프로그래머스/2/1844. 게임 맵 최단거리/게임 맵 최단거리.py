from collections import deque

def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    q = deque([(0,0,1)])
    visited[0][0] = True
    while q:
        cx, cy, dist = q.popleft()
        
        if cx == n-1 and cy == m-1:
            return dist
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = True
                
    return -1