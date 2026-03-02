from collections import deque
from itertools import combinations

def spread(board):
  q = deque(virus)

  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
        board[nx][ny] = 2
        q.append((nx,ny))

  return sum(row.count(0) for row in board)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

virus = deque()
empty_spaces = set()

for r in range(n):
  for c in range(m):
    if board[r][c] == 2:
      virus.append((r,c))
    elif board[r][c] == 0:
      empty_spaces.add((r,c))

ans = 0
for walls in combinations(empty_spaces, 3):
  (x1, y1), (x2, y2), (x3, y3) = walls
  new_board = [row[:] for row in board]
  new_board[x1][y1], new_board[x2][y2], new_board[x3][y3] = 1, 1, 1
  
  ans = max(ans, spread(new_board))

print(ans)