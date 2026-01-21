import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
is_merged = [[False] * n for _ in range(n)]

# 왼쪽으로 밀기
def move_left(cur_board, n):
  new_board = []
  for r in range(n):
    # 현재 행에서 0이 아닌 숫자들 모으기
    row = [val for val in cur_board[r] if val != 0]

    new_row = []
    skip = False
    for i in range(len(row)):
      # 합쳐진 블록이 또 합쳐지지 않게 skip
      if skip:
        skip = False
        continue
      if i + 1 < len(row) and row[i] == row[i+1]:
        new_row.append(row[i] * 2)
        skip = True
      else:
        new_row.append(row[i])

    while len(new_row) < n:
      new_row.append(0)
    new_board.append(new_row)

  return new_board

def move_right(cur_board, n):
  new_board = [row[::-1] for row in cur_board]
  new_board = move_left(new_board,n)
  return [row[::-1] for row in new_board]

def move_up(cur_board, n):
  new_board = [[0] * n for _ in range(n)]

  for c in range(n):
    # 현재 열에서 0이 아닌 숫자들 모으기
    col = []
    for r in range(n):
      if cur_board[r][c] != 0:
        col.append(cur_board[r][c])

    new_col = []
    skip = False
    for i in range(len(col)):
      if skip:
        skip = False
        continue
      if i + 1 < len(col) and col[i] == col[i+1]:
        new_col.append(col[i] * 2)
        skip = True
      else:
        new_col.append(col[i])

    while len(new_col) < n:
      new_col.append(0)

    for r in range(len(new_col)):
      new_board[r][c] = new_col[r]
        
  return new_board

def move_down(cur_board, n):
  new_board = cur_board[::-1]
  new_board = move_up(new_board, n)
  return new_board[::-1]

ans = 0
def dfs(count, cur_board):
  global ans
  n = len(cur_board)
  # 5번 돌았으면 최댓값 찾고 종료
  if count == 5:
    cur_max = max(max(row) for row in cur_board)
    ans = max(ans, cur_max)
    return

  for i in range(4):
    nxt_board = []
    if i == 0:
      nxt_board = move_left(cur_board, n)
    elif i == 1:
      nxt_board = move_right(cur_board, n)
    elif i == 2:
      nxt_board = move_up(cur_board, n)
    else:
      nxt_board = move_down(cur_board, n)
    dfs(count+1, nxt_board)


dfs(0, board)
print(ans)