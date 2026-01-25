def find_heart():
  hx, hy = 0, 0
  for r in range(N):
    for c in range(N):
      if board[r][c] == '*':
        for i in range(4):
          nr, nc = r+dx[i], c+dy[i]
          if nr<0 or N<=nr or nc<0 or N<=nc or board[nr][nc] != '*':
            break
          elif i == 3:
            hx, hy = r, c
  return hx, hy

def measure(x, y, i):
  # i) 0:왼쪽 1:오른쪽 2:아래
  nx, ny = x, y
  length = 1
  while True:
    nx, ny = nx + dx[i], ny + dy[i]
    if nx<0 or N<=nx or ny<0 or N<=ny or board[nx][ny] != '*':
      break
    length += 1

  return length

N = int(input())
board = [list(input()) for _ in range(N)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]

hx, hy = find_heart()
la = measure(hx,hy-1,0)
ra = measure(hx,hy+1,1)
w = measure(hx+1,hy,2)
ll = measure(hx+w+1,hy-1,2)
rl = measure(hx+w+1,hy+1,2)

print(hx+1, hy+1)
print(la, ra, w, ll, rl)