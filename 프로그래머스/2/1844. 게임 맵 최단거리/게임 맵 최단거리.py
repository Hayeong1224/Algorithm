from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    q = deque([(0, 0, 1)])
    visited = set()
    visited.add((0,0))
    
    while q:
        cx, cy, dist = q.popleft()
        if cx == n-1 and cy == m-1:
            return dist
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny,dist+1))
        
    return -1