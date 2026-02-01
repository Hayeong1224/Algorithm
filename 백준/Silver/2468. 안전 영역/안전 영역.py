from collections import deque

def bfs(x, y, h):
  q = deque([(x,y)])
  visited[x][y] = True

  while q:
    r, c = q.popleft()
    for i in range(4):
      nr, nc = r + dx[i], c + dy[i]
      if 0<=nr<N and 0<=nc<N and board[nr][nc] > h and not visited[nr][nc]:
          q.append((nr,nc))
          visited[nr][nc] = True  

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

max_v = max(board[r][c] for r in range(N) for c in range(N))

max_cnt = 0
for h in range(max_v):
  cnt = 0
  visited = [[False] * N for _ in range(N)]
  for r in range(N):
    for c in range(N):
      if board[r][c] > h and not visited[r][c]:
        cnt += 1
        bfs(r,c,h)

  max_cnt = max(max_cnt, cnt)

print(max_cnt)