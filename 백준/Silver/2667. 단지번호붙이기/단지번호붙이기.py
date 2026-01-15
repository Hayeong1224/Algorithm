from collections import deque

n = int(input())
village = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
  visited[x][y] = True
  count = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<n:
      if not visited[nx][ny] and village[nx][ny] == 1:
        count += dfs(nx, ny)

  return count
  
result = []
for i in range(n):
  for j in range(n):
    if not visited[i][j] and village[i][j] == 1:
      result.append(dfs(i,j))

result.sort()
print(len(result))
for r in result:
  print(r)