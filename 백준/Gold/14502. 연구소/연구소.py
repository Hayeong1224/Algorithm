from collections import deque
from itertools import combinations

def spread(b):
  q = deque(queue)
  v = [line[:] for line in visited]
  
  while q:
    x, y = q. popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0<=nx<N and 0<=ny<M and not v[nx][ny] and b[nx][ny] == 0:
        v[nx][ny] = True
        b[nx][ny] = 2
        q.append((nx,ny))
  
  return sum(line.count(0) for line in b) # 안전영역 크기

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 벽 세울 때마다 위치 변하는게 아니니까 한 번만!
queue = deque() 
visited = [[False] * M for _ in range(N)]
empty_spaces = set()

for i in range(N):
  for j in range(M):
    if board[i][j] == 2:
      queue.append((i,j))
      visited[i][j] = True
    elif board[i][j] == 0:
      empty_spaces.add((i,j))

ans = 0
# 벽 세우기
for walls in combinations(empty_spaces,3):
  (x1,y1),(x2,y2),(x3,y3) = walls
  new_board = [line[:] for line in board]
  new_board[x1][y1], new_board[x2][y2], new_board[x3][y3] = 1, 1, 1
    
  # 퍼뜨리기
  ans = max(ans,spread(new_board))
  
print(ans)