import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 구슬을 벽 끝까지 미는 함수
def move(x, y, dx, dy, board):
  count = 0
  while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
    x += dx
    y += dy
    count += 1
  return x, y, count


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 방문 처리용 4차원 배열 (rx, ry, bx, by)
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
  for j in range(m):
    if board[i][j] == 'R':
      rx, ry = i, j
    elif board[i][j] == 'B':
      bx, by = i, j

# bfs
q = deque()
q.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = True

while q:
  curr_rx, curr_ry, curr_bx, curr_by, count = q.popleft()

  if count >= 10:
    break

  for i in range(4):
    nrx, nry, r_cnt = move(curr_rx, curr_ry, dx[i], dy[i], board)
    nbx, nby, b_cnt = move(curr_bx, curr_by, dx[i], dy[i], board)

    # 실패: 파란 구슬이 빠지면 다음 방향으로
    if board[nbx][nby] == 'O':
      continue

    if board[nrx][nry] == 'O':
      print(count + 1)
      exit()

    if nrx == nbx and nry == nby:
      if r_cnt > b_cnt:
        nrx -= dx[i]
        nry -= dy[i]
      else:
        nbx -= dx[i]
        nby -= dy[i]

    if not visited[nrx][nry][nbx][nby]:
      visited[nrx][nry][nbx][nby] = True
      q.append((nrx, nry, nbx, nby, count+1))

print(-1)