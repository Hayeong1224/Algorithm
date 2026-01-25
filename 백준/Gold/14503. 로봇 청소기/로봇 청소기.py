N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d: 0북 1동 2남 3서
board = [list(map(int, input().split())) for _ in range(N)] # 0: 청소 안 된 빈칸, 1: 벽

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
  if board[r][c] == 0:
    board[r][c] = 2 # 청소한 칸
  
  # 주변 4칸 확인
  check = False
  for i in range(4):
    nr, nc = r + dx[i], c + dy[i]
    if 0<=nr<N and 0<=nc<M and board[nr][nc] == 0:
      check = True

  # 빈 칸이 있는 경우
  if check:
    for i in range(4):
      d = (d+3) % 4 # 반시계 방향 90도 회전
      nr, nc = r + dx[d], c + dy[d]
      if 0<=nr<N and 0<=nc<M and board[nr][nc] == 0:
        r, c = nr, nc # 한 칸 전진
        break

  # 빈 칸이 없는 경우
  else: 
    nr, nc = r + dx[(d+2)%4], c + dy[(d+2)%4] # 뒷 칸 살펴보기
    if 0<=nr<N and 0<=nc<M and board[nr][nc] != 1:
      r, c = nr, nc # 한 칸 후진
    else: # 뒤가 벽인 경우
      break

print(sum(line.count(2) for line in board))