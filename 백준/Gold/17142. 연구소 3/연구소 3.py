from collections import deque
from itertools import combinations

def spread(active, b, total_empty):
  dist = [[-1] * N for _ in range(N)]
  q = deque()

  for r,c in active:
    dist[r][c] = 0
    q.append((r,c))

  max_time = 0
  activated_empty = 0
  
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0<=nx<N and 0<=ny<N and b[nx][ny] != 1:
        if dist[nx][ny] == -1: # 미방문
          dist[nx][ny] = dist[cx][cy] + 1

          if b[nx][ny] == 0: # 빈 칸이면 시간 업데이트 및 카운트
            activated_empty += 1
            max_time = dist[nx][ny]

          q.append((nx,ny))

  return max_time if activated_empty == total_empty else float('inf')

N, M = map(int, input().split())
board = []
virus = []
empty_count = 0

for r in range(N):
  row = list(map(int, input().split()))
  for c in range(N):
    if row[c] == 0:
      empty_count += 1
    elif row[c] == 2:
      virus.append((r,c))
  board.append(row)

if empty_count == 0:
  print(0)
  exit()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = float('inf')
for active in combinations(virus, M):
  ans = min(ans, spread(active, board, empty_count))

print(ans if ans != float('inf') else -1)