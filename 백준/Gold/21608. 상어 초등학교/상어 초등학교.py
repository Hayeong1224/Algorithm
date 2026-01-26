N = int(input())
# 0: 자기 번호, 1/2/3/4: 좋아하는 학생 번호
students = [list(map(int, input().split())) for _ in range(N**2)]
board = [[0] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N**2):
  max_f, max_status = 0, []
  for r in range(N):
    for c in range(N):
      if board[r][c] != 0:
        continue
      # 인접한 좋아하는 학생 수, 인접 빈 칸 수 세기
      favorites, empty_seats = 0, 0
      for k in range(4):
        nr, nc = r + dx[k], c + dy[k]
        if 0<=nr<N and 0<=nc<N:
          if board[nr][nc] == 0:
            empty_seats += 1
          elif board[nr][nc] in students[i][1:]:
            favorites += 1
      if max_f == favorites:
        max_status.append([r, c, empty_seats])
      elif max_f < favorites:
        max_f, max_status = favorites, [[r, c, empty_seats]]

  max_status.sort(key= lambda x : (-x[2],x[0],x[1]))
  board[max_status[0][0]][max_status[0][1]] = students[i][0]

ans = 0

for i in range(N**2):
  x,y = next((r,c) for r in range(N) for c in range(N) if board[r][c] == students[i][0])

  favorites = 0
  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]
    if 0<=nx<N and 0<=ny<N:
      if board[nx][ny] in students[i][1:]:
        favorites += 1

  ans += 10 ** (favorites-1) if favorites > 0 else 0

print(ans)