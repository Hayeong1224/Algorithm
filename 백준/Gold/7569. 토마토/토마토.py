from collections import deque
m, n, h = map(int, input().split()) # 가로, 세로, 높이
boxes = []
q = deque()

for i in range(h):
  level = []
  for j in range(n):
    row = list(map(int, input().split()))
    for k in range(m):
      if row[k] == 1: # 익은 토마트들 큐에 미리 넣기
        q.append((i,j,k))
    level.append(row)
  boxes.append(level)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
  while q:
    cz, cx, cy = q.popleft()
    for i in range(6):
      nz, nx, ny = cz + dz[i], cx + dx[i], cy + dy[i]
      if 0<=nz<h and 0<=nx<n and 0<=ny<m:
        if boxes[nz][nx][ny] == 0:
          boxes[nz][nx][ny] = boxes[cz][cx][cy] + 1
          q.append((nz,nx,ny))

bfs()

max_days = 0
for level in boxes:
  for row in level:
    for tomato in row:
      if tomato == 0: # 히나라도 안 익은 상황
        print(-1)
        exit()
      max_days = max(max_days, tomato)  

print(max_days - 1) # 처음부터 익어있었으면 다 1이니까 0 출력