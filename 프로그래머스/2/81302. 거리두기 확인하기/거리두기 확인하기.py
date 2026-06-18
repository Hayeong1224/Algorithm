from collections import deque
dx = [0, -1, 0, 1]
dy = [1, 0, -1 ,0]

def is_possible(board, r, c):
    # distance가 3 이상이 되거나 파티션이면 큐에 넣지 말기
    n = len(board)
    q = deque([(r,c,0)])
    visited = set()
    visited.add((r,c))
    
    while q:
        cx, cy, dist = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited:
                if dist + 1 <= 2 and board[nx][ny] != 'X':
                    if board[nx][ny] == 'P':
                        return False
                    else:
                        visited.add((nx,ny))
                        q.append((nx,ny,dist+1))
    return True        

def solution(places):
    answer = []
    
    for room in places:
        n = len(room)
        
        keep_checking = True
        for r in range(n):
            for c in range(n):
                if room[r][c] == 'P': # 거리 2 이하에 p가 있는지 확인
                    keep_checking = is_possible(room, r, c)
                    if not keep_checking:   break
            
            if not keep_checking:
                answer.append(0)
                break
                
        if keep_checking:
            answer.append(1)
    
    return answer