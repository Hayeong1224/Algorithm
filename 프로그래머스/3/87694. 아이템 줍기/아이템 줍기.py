from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 일단 가능 경로를 찾기
    board = [[0] * 102 for _ in range(102)]
    
    # 테두리 때문에 경로 아닌 곳으로 갈 수 ㅇ -> 좌표값 2배
    for lx, ly, rx, ry in rectangle:
        lx *= 2
        ly *= 2
        rx *= 2
        ry *= 2
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                board[x][y] = 1
                
    # 겹치는 부분 파내기
    for lx, ly, rx, ry in rectangle:
        lx *= 2
        ly *= 2
        rx *= 2
        ry *= 2
        for x in range(lx + 1, rx):
            for y in range(ly + 1, ry):
                board[x][y] = 0
    
    # 좌표 두 배
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    # 이후 bfs로 찾기
    q = deque([(characterX, characterY, 0)])
    visited = set()
    visited.add((characterX,characterY))
    
    while q:
        cx, cy, dist = q.popleft()
        if cx == itemX and cy == itemY:
            return dist // 2
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<102 and 0<=ny<=102 and board[nx][ny] and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx, ny, dist+1))
    
    return -1  