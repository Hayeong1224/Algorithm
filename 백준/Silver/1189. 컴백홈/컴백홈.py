r, c, k = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y, dist):
  if x == 0 and y == c-1:
    return 1 if dist == k else 0

  ans = 0
  visited[x][y] = True
    
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    
    if 0 <= nx < r and 0 <= ny < c: 
      if not visited[nx][ny] and board[nx][ny] != 'T':
        ans += dfs(nx, ny, dist + 1)
  
  visited[x][y] = False
  return ans

print(dfs(r-1,0,1))