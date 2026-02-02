from collections import deque

def get_icebergs():
  ice = []
  for r in range(N):
    for c in range(M):
      if board[r][c] > 0:
        ice.append((r,c))
  return ice

def melt(ice_list):
  melt_list = []
  for r, c in ice_list:
    cnt = 0
    for i in range(4):
      nr, nc = r + dx[i], c + dy[i]
      if 0<=nr<N and 0<=nc<M and board[nr][nc] == 0:
        cnt += 1

    melt_list.append((r, c, cnt))

  for r, c, cnt in melt_list:
    board[r][c] = max(0, board[r][c] - cnt)

def check_group(ice_list):
  if not ice_list:
    return 0
  
  visited = [[False] * M for _ in range(N)]
  cnt = 0

  for r, c in ice_list:
    if board[r][c] > 0 and not visited[r][c]:
      cnt += 1
      q = deque([(r,c)])
      visited[r][c] = True
      while q:
        x,y = q.popleft()
        for i in range(4):
          nx, ny = x + dx[i], y + dy[i]
          if 0<=nx<N and 0<=ny<M and board[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx,ny))

  return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

year = 0
while True:
  ice_list = get_icebergs()

  groups = check_group(ice_list)

  if groups >= 2:
    print(year)
    break
    
  if groups == 0: # 다 녹은 경우
    print(0)
    break

  melt(ice_list)
  year += 1