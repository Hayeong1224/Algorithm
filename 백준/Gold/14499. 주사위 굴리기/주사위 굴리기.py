def roll(dir, dice):
  if dir == 1: # 동쪽 -> d: r, r: u
    temp = dice[1]
    dice[1] = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = temp
  elif dir == 2: # 서쪽 -> d: l, r: d
    temp = dice[1]
    dice[1] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = temp
  elif dir == 3: # 북쪽 -> d: b, r: r
    temp = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[0]
    dice[0] = dice[4]
    dice[4] = temp
  else: # 남쪽 -> d: f,r: r
    temp = dice[1]
    dice[1] = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[5]
    dice[5] = temp

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

# 1동 2서 3북 4남
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
# 0위, 1아래, 2왼쪽, 3오른쪽, 4앞, 5뒤
dice = [0,0,0,0,0,0]

for dir in cmd:
  nx, ny = x + dx[dir], y + dy[dir]
  if nx < 0 or N <= nx or ny < 0 or M <= ny:
    continue
    
  roll(dir, dice)
  if board[nx][ny] == 0:
    board[nx][ny] = dice[1]
  else:
    dice[1] = board[nx][ny]
    board[nx][ny] = 0
  print(dice[0])
  x, y = nx, ny