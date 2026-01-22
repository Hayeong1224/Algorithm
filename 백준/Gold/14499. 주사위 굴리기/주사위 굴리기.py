import sys
input = sys.stdin.readline

def roll(dir, d):
  if dir == 1: # 동
    d[0], d[1], d[2], d[3] = d[2], d[3], d[1], d[0]
  elif dir == 2: # 서
    d[0], d[1], d[2], d[3] = d[3], d[2], d[0], d[1]
  elif dir == 3: # 북
    d[0], d[1], d[4], d[5] = d[4], d[5], d[1], d[0]
  else: # 남
    d[0], d[1], d[4], d[5] = d[5], d[4], d[0], d[1]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

# 0위, 1아래, 2왼쪽, 3오른쪽, 4앞, 5뒤
dice = [0] * 6
# 1동 2서 3북 4남
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

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