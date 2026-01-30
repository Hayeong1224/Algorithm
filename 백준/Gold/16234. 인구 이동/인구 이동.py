import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
  global unions, visited
  union = []
  q = deque([(r,c)])
  visited[r][c] = True
  union.append((r,c))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <=  abs(A[x][y] - A[nx][ny]) <= R:
        q.append((nx,ny))
        visited[nx][ny] = True
        union.append((nx,ny))

  unions.append(union)


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
while True:
  unions = list() # unions[i] = [(r,c), (r2,c2), ...]
  visited = [[False] * N for _ in range(N)]
  for r in range(N):
    for c in range(N):
      if not visited[r][c]:
        bfs(r,c)

  if len(unions) == N*N:
    print(ans)
    break
  else:
    ans += 1
    # 인구 이동
    for union in unions:
      n = len(union)
      total = sum(A[x][y] for x, y in union)
      for x, y in union:
        A[x][y] = total // n