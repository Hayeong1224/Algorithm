N = int(input())
dx = [1, 0, -1, 0] # 우 상 좌 하
dy = [0, -1, 0, 1] # x = 열, y = 행

board = [[False] * 101 for _ in range(101)]
for _ in range(N):
  x, y, d, g = map(int, input().split())

  # 드래곤 커브의 방향 리스트 만들기
  move_dir = [d]
  for _ in range(g):
    # 현재까지의 방향을 뒤에서부터 꺼내서 90도 회전 후 추가
    for i in range(len(move_dir) -1, -1, -1):
      move_dir.append((move_dir[i] + 1) % 4)

  # 보드에 점 찍기
  board[y][x] = True
  for dir in move_dir:
    x += dx[dir]
    y += dy[dir]
    if 0 <= x <= 100 and 0 <= y <= 100:
      board[y][x] = True

# 사각형 개수 세기
ans = 0
for i in range(100):
  for j in range(100):
    if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
        ans += 1

print(ans)