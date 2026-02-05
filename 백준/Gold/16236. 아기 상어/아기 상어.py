from collections import deque

def find_shark():
  for r in range(n):
    for c in range(n):
      if space[r][c] == 9:
        return r, c

  return -1, -1 # 이런 경우 x

def find_target(sx, sy, ss):
  dist = [[-1] * n for _ in range(n)]
  q = deque([(sx, sy)])
  dist[sx][sy] = 0

  candidates = []

  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]

      if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
        # 지나갈 수 있음
        if space[nx][ny] <= ss:
          dist[nx][ny] = dist[cx][cy] + 1
          q.append((nx,ny))
          # 먹을 수 있음
          if 0 < space[nx][ny] < ss:
            candidates.append((dist[nx][ny],nx,ny))

  if not candidates:
    return None

  candidates.sort()
  return candidates[0]

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

# 아기 상어 찾기
shark_x, shark_y = find_shark()
space[shark_x][shark_y] = 0

shark_size = 2
time, count_eat = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 물고기 더 잡아먹을 수 있는지
while True:
  target = find_target(shark_x, shark_y, shark_size)

  if target is None:
    break
    
  dist, x, y = target

  time += dist
  shark_x, shark_y = x, y
  space[shark_x][shark_y] = 0
  count_eat += 1
  
  if count_eat == shark_size:
    shark_size += 1
    count_eat = 0
  
print(time)