from collections import deque
n = int(input())
picture = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def bfs(x, y):
  q = deque([(x,y)])
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and picture[cx][cy] == picture[nx][ny]:
        q.append((nx,ny))
        visited[nx][ny] = True
  return 1

# 적록색약 x
count1 = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      count1 += bfs(i,j)
        
# 적록색약
for i in range(n):
  for j in range(n):
    if picture[i][j] == 'G':
      picture[i][j] = 'R'
    if visited[i][j]:
      visited[i][j] = False

count2 = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      count2 += bfs(i,j)

print(count1, count2)