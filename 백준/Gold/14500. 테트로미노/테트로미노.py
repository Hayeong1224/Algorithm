def dfs(n, sm, temp_list):
  global ans
  if n == 4: # 블럭 4개면 끝
    ans = max(ans, sm)
    return 

  for tx, ty in temp_list:
    for i in range(4):
      nx, ny = tx + dx[i], ty + dy[i]
      if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
        visited[nx][ny] = 1
        dfs(n+1, sm+board[nx][ny], temp_list + [(nx,ny)])
        visited[nx][ny] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
for i in range(N):
  for j in range(M): # 모든 위치에서 DFS 탐색
    visited[i][j] = 1
    dfs(1, board[i][j], [(i,j)])

print(ans) 