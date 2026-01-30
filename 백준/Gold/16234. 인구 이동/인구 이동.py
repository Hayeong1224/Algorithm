import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
  global visited
  union = [(r,c)]
  q = deque([(r,c)])
  visited[r][c] = True
  total_population = A[r][c]

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <=  abs(A[x][y] - A[nx][ny]) <= R:
        visited[nx][ny] = True
        q.append((nx,ny))
        union.append((nx,ny))
        total_population += A[nx][ny]

  if len(union) > 1:
    avg = total_population // len(union)
    for x, y in union:
      A[x][y] = avg
    return True
  return False

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
while True:
  visited = [[False] * N for _ in range(N)]
  moved = False
  
  for r in range(N):
    for c in range(N):
      if not visited[r][c]:
        if bfs(r,c):
          moved = True

  if not moved:
    break
  ans += 1

print(ans)