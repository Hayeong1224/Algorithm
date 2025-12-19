from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0,0,1)])
    maps[0][0] = 0
        
    while queue:
        x, y, d = queue.popleft()
        
        if x == n-1 and y == m-1:
            return d
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx,ny,d+1))
    return -1