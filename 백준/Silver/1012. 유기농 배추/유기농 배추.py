from collections import deque
T = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def bfs(x, y):
  q = deque([(x,y)])
  field[x][y] = 0
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<m and 0<=ny<n and field[nx][ny] == 1:
        q.append((nx,ny))
        field[nx][ny] = 0
  
  return 1

for _ in range(T):
  m, n, k = map(int, input().split())
  field = [[0] * 50 for _ in range(50)]
  for _ in range(k):
    x, y = map(int, input().split())
    field[x][y] = 1
  
  count = 0
  for i in range(m):
    for j in range(n):
      if field[i][j] == 1:
        count += bfs(i,j)

  print(count)