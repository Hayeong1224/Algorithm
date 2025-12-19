from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 사각형 내부라면 0
                if x1 < i < x2 and y1 < j < y2:
                    grid[i][j] = 0
                # 테두리라면 (이미 내부(0)로 판정된 곳이 아닐 때만 1로 표시)
                elif grid[i][j] != 0:
                    grid[i][j] = 1
    
    queue = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[0] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 1
    
    while queue:
        x, y, d = queue.popleft()
        if x == itemX * 2and y == itemY * 2:
            return d // 2
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102 and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny,d+1))
                
    return -1 #사실 이럴 경우는 x 