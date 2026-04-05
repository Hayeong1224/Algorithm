from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 일단 테두리 구하기
    board = [[0] * 101 for _ in range(101)]
    for x1, y1, x2, y2 in rectangle: # 채우기
        for x in range(x1*2, x2*2 + 1):
            for y in range(y1*2, y2*2 + 1):
                board[x][y] = 1
    
    for x1, y1, x2, y2 in rectangle: # 파내기
        for x in range(x1*2 + 1, x2*2):
            for y in range(y1*2 + 1, y2*2):
                board[x][y] = 0
    
    # dx, dy 움직이면서 bfs하기
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    board[characterX * 2][characterY * 2] = 0
    
    while q:
        cx, cy, dist = q.popleft()
        if cx == itemX * 2 and cy == itemY * 2:
            return dist // 2
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<101 and 0<=ny<101 and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx,ny,dist+1))
    
    return -1