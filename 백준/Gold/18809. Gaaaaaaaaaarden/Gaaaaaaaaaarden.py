from itertools import combinations
from collections import deque

def spread(green_selection, red_selection):
  # (시간, 색) 0: 빈 칸, 1: 초록, 2: 빨강, 3: 꽃
  state = [[(0,0) for _ in range(M)] for _ in range(N)]
  q = deque()
  
  for r,c in green_selection:
    q.append((r,c))
    state[r][c] = (0,1)
    
  for r,c in red_selection:
    q.append((r,c))
    state[r][c] = (0,2)
  
  cnt = 0
  while q:
    cx, cy = q.popleft()
    ctime, ccolor = state[cx][cy]

    if ccolor == 3: # 이미 꽃이면 중지
      continue
    
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if 0<=nx<N and 0<=ny<M and board[nx][ny] != 0:
        if state[nx][ny][1] == 0: # 첫 방문 -> 확산
          state[nx][ny] = (ctime + 1, ccolor)
          q.append((nx,ny))

        elif state[nx][ny][0] == ctime + 1 and ((state[nx][ny][1] == 1 and ccolor == 2) or (state[nx][ny][1] == 2 and ccolor == 1)): # 꽃
          state[nx][ny] = (ctime + 1, 3)
          cnt += 1

  return cnt

N, M, G, R = map(int, input().split())
board = [] # 0: 호수, 1: 뿌릴 수 없는 땅, 2: 뿌릴 수 있는 땅

pos = []
for r in range(N):
  row = list(map(int, input().split()))
  for c in range(M):
    if row[c] == 2:
      pos.append((r,c))      
  board.append(row)
  
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
# G와 R 뿌릴 자리 정하기
for total_selection in combinations(pos, G + R):
  for green_selection in combinations(total_selection, G):
    red_selection = [ cell for cell in total_selection if cell not in green_selection]
    
    ans = max(ans, spread(green_selection, red_selection))

print(ans)